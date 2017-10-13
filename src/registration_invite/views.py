
from django.db import transaction
from django.shortcuts import redirect
from django.urls import reverse
from django.views.generic import FormView, TemplateView
from registration import signals
from registration.backends.hmac.views import ActivationView as BaseActivationView
from registration.backends.hmac.views import RegistrationView

from .forms import ActivationForm, InvitationForm

__all__ = (
    'InvitationView', 'InvitationCompleteView',
    'ActivationView', 'ActivationCompleteView',
)


class InvitationView(RegistrationView):
    template_name = 'registration/invite/invitation_form.html'
    form_class = InvitationForm

    email_body_template = 'registration/invite/email_body.txt'
    email_subject_template = 'registration/invite/email_subject.txt'

    @property
    def current_app(self):
        return self.request.resolver_match.app_name

    def get_success_url(self, user):
        return reverse('invitation_complete', current_app=self.current_app)

    def get_activation_url(self, activation_key):
        path = reverse('activate',
                       kwargs={'activation_key': activation_key},
                       current_app=self.current_app)
        return self.request.build_absolute_uri(path)

    def get_email_context(self, activation_key):
        context = super().get_email_context(activation_key)
        context['activation_url'] = self.get_activation_url(activation_key)
        return context

    @transaction.atomic
    def create_inactive_user(self, form):
        new_user = form.save(commit=False)
        new_user.is_active = False
        new_user.set_unusable_password()
        new_user.save()

        self.send_activation_email(new_user)

        return new_user


class InvitationCompleteView(TemplateView):
    template_name = 'registration/invite/invitation_complete.html'


class ActivationView(BaseActivationView, FormView):
    template_name = 'registration/invite/activation_form.html'
    form_class = ActivationForm

    def get_context_data(self, **kwargs):
        context = super(ActivationView, self).get_context_data(**kwargs)
        context['instance'] = context['form'].instance
        return context

    def get_form_kwargs(self):
        kwargs = super(ActivationView, self).get_form_kwargs()
        username = self.validate_key(kwargs.get('activation_key'))
        if username:
            kwargs['instance'] = self.get_user(username)

        return kwargs

    def get(self, *args, **kwargs):
        return super(FormView, self).get(*args, **kwargs)

    @transaction.atomic
    def form_valid(self, form):
        activated_user = self.activate(*self.args, **self.kwargs)
        if activated_user:
            # We need to update the activated user with the form's cleaned_data since
            # since calling form.save() will overwrite the activated user.
            activated_user.__dict__.update(form.cleaned_data)
            activated_user.save()
            signals.user_activated.send(sender=self.__class__,
                                        user=activated_user,
                                        request=self.request)
            success_url = self.get_success_url(activated_user)
            try:
                to, args, kwargs = success_url
                return redirect(to, *args, **kwargs)
            except ValueError:
                return redirect(success_url)
        return super(ActivationView, self).get(*args, **kwargs)

    def get_success_url(self, user):
        current_app = self.request.resolver_match.app_name
        return reverse('activation_complete', current_app=current_app)


class ActivationCompleteView(TemplateView):
    template_name = 'registration/invite/activation_complete.html'

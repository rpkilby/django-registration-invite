
from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from django.urls import reverse

from . import forms, views

User = get_user_model()

admin.site.unregister(User)


class AdminInvitationView(views.InvitationView):
    template_name = 'admin/registration_invitation.html'

    def get_context_data(self, **kwargs):
        form = self.get_form(self.get_form_class())

        context = super(AdminInvitationView, self).get_context_data(**kwargs)
        context['opts'] = get_user_model()._meta
        context['adminform'] = admin.helpers.AdminForm(
            form, [(None, {'fields': [field.name for field in form]})], {},
        )
        return context

    def get_success_url(self, user):
        return reverse(
            'admin:%s_%s_changelist' % (User._meta.app_label, User._meta.model_name, ),
        )


@admin.register(User)
class UserInvitationAdmin(UserAdmin):

    def get_invitation_form(self):
        return forms.InvitationForm

    def get_urls(self):
        invitation_view = AdminInvitationView.as_view(form_class=self.get_invitation_form())
        return [
            url(r'^invite/$', self.admin_site.admin_view(invitation_view), name='registration_invitation'),
        ] + super(UserInvitationAdmin, self).get_urls()

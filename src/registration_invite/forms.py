
from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

User = get_user_model()


class InvitationForm(forms.ModelForm):
    class Meta:
        model = User
        fields = (User.USERNAME_FIELD, User.EMAIL_FIELD) + tuple(User.REQUIRED_FIELDS)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields[User.EMAIL_FIELD].required = True


class ActivationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('password1', 'password2')

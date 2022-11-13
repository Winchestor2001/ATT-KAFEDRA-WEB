from django.contrib.auth.models import User
from django.forms import ModelForm


class SignUpForm(ModelForm):
    class Meta:
        model = User
        fields = ["username", "email", "first_name", "last_name", "password"]


class SignInForm(ModelForm):
    class Meta:
        model = User
        fields = ["username", "password"]

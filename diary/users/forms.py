from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import Group
from .models import User

class RegisterForm(UserCreationForm):
    group = forms.ModelChoiceField(
        queryset=Group.objects.all(),
        required=True,
        label="Group"
    )

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', 'group')
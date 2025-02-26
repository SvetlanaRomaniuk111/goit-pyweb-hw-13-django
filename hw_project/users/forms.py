from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.forms import CharField, TextInput, EmailInput, EmailField, \
    PasswordInput


class RegisterForm(UserCreationForm):
    username = CharField(max_length=16, min_length=3, required=True,
                         widget=TextInput(attrs={"class": "form-control",
                                                 "placeholder": "Enter username"}))
    email = EmailField(max_length=25, required=True, widget=EmailInput(
        attrs={"class": "form-control", "placeholder": "Enter email"}))
    password1 = CharField(required=True,
                          widget=PasswordInput(attrs={"class": "form-control", "placeholder": "Enter password"}))
    password2 = CharField(required=True,
                          widget=PasswordInput(attrs={"class": "form-control", "placeholder": "Repeat password"}))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class LoginForm(AuthenticationForm):
    username = CharField(max_length=16, min_length=3, required=True,
                         widget=TextInput(attrs={"class": "form-control",
                                                 "placeholder": "Enter username"}))
    password = CharField(required=True,
                         widget=PasswordInput(attrs={"class": "form-control", "placeholder": "Enter password"}))

    class Meta:
        model = User
        fields = ('username', 'password')

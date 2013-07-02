#encoding=utf-8
from django.forms import ModelForm
from movie.models import User


class RegisterForm(ModelForm):
    class Meta:
        model = User

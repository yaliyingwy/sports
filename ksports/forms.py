#encoding=utf-8
from django.forms import ModelForm
from django import forms
from ksports.models  import Person


class PersonForm(ModelForm):
    name = forms.CharField(error_messages={'required': '姓名不能为空'})
    class Meta:
        model = Person
        exclude = ('name',)

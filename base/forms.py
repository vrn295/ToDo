from django import forms
from django.forms import ModelForm

from .models import *


class BaseForm(forms.ModelForm):
    class Meta:
        model = Base
        fields = '__all__'

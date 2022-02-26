from dataclasses import fields
from django.forms import ModelForm
from .models import nums
class NumsForm(ModelForm):
  class Meta:
    model=nums
    fields='__all__'
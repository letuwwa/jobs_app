from django import forms
from .models import (
    CVModel,
)


class CVModelForm(forms.ModelForm):
    class Meta:
        model = CVModel
        fields = ('position', )

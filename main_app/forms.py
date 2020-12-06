from django import forms
from .models import (
    CVModel,
)


class CVModelForm(forms.ModelForm):
    class Meta:
        model = CVModel
        fields = ('position', 'salary', 'personal_info', 'skills', 'selected_language')

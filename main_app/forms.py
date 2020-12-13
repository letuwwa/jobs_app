from django import forms
from .models import (
    CVModel,
    JobModel,
)


class CVModelForm(forms.ModelForm):
    class Meta:
        model = CVModel
        fields = ('position', 'salary', 'personal_info', 'skills', 'selected_language')


class JobModelForm(forms.ModelForm):
    class Meta:
        model = JobModel
        fields = ('job_position', 'job_salary', 'about_worker', 'skills')

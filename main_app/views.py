from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    CreateView,
    UpdateView,
    DeleteView,
    View,
    TemplateView,
    DetailView,
)
from .models import CVModel, JobModel
from .forms import CVModelForm, JobModelForm


def index(request):
    return render(request, 'base.html', context={})


class CVCreate(CreateView):
    template_name = 'cv/cv_create.html'
    model = CVModel
    form_class = CVModelForm


class CVUpdate(UpdateView):
    template_name = 'cv/cv_create.html'
    model = CVModel
    form_class = CVModelForm


class CVListView(ListView):
    template_name = 'cv/cv_list.html'
    model = CVModel
    context_object_name = 'cv_list'


class CVDetail(DetailView):
    model = CVModel
    template_name = 'cv/cv_detail.html'
    context_object_name = 'cv'


class CVDelete(DeleteView):
    model = CVModel
    success_url = reverse_lazy('cv_list')
    template_name = 'confirm_delete.html'


class JobCreate(CreateView):
    template_name = 'job/job_create.html'
    model = JobModel
    form_class = JobModelForm


class JobUpdate(UpdateView):
    template_name = 'job/job_create.html'
    model = JobModel
    form_class = JobModelForm


class JobListView(ListView):
    template_name = 'job/job_list.html'
    model = JobModel
    context_object_name = 'job_list'


class JobDetail(DetailView):
    model = JobModel
    template_name = 'job/job_detail.html'
    context_object_name = 'job'


class JobDelete(DeleteView):
    model = JobModel
    success_url = reverse_lazy('job_list')
    template_name = 'confirm_delete.html'

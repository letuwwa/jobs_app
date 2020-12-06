from django.shortcuts import render
from django.views.generic import (
    ListView,
    CreateView,
    UpdateView,
    DeleteView,
    View,
    TemplateView,
    DetailView,
)
from .models import CVModel
from .forms import CVModelForm


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

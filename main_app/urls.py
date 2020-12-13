from django.urls import path, include
from .views import *

urlpatterns = [
    path('cv_create/', CVCreate.as_view(), name='cv_create'),
    path('cv_list/', CVListView.as_view(), name='cv_list'),
    path('cv_update/<int:pk>/', CVUpdate.as_view(), name='cv_update'),
    path('cv_detail/<int:pk>/', CVDetail.as_view(), name='cv_detail'),
    path('cv_delete/<int:pk>/', CVDelete.as_view(), name='cv_delete'),
    path('job_create/', JobCreate.as_view(), name='job_create'),
    path('job_list/', JobListView.as_view(), name='job_list'),
    path('job_update/<int:pk>/', JobUpdate.as_view(), name='job_update'),
    path('job_detail/<int:pk>/', JobDetail.as_view(), name='job_detail'),
    path('job_delete/<int:pk>/', JobDelete.as_view(), name='job_delete'),
    path('', index, name='index'),
    path('', include('django.contrib.auth.urls')),
]
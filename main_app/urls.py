from django.urls import path, include
from .views import (
    index,
    CVCreate,
    CVUpdate
)

urlpatterns = [
    path('cv_create/', CVCreate.as_view(), name='cv_create'),
    path('cv_update/<int:pk>/', CVUpdate.as_view(), name='cv_update'),
    path('', index, name='index'),
    path('', include('django.contrib.auth.urls')),
]
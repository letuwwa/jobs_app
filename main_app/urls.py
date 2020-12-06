from django.urls import path, include
from .views import (
    index,
    CVCreate,
    CVUpdate,
    CVDetail,
    CVListView
)

urlpatterns = [
    path('cv_create/', CVCreate.as_view(), name='cv_create'),
    path('cv_list/', CVListView.as_view(), name='cv_list'),
    path('cv_update/<int:pk>/', CVUpdate.as_view(), name='cv_update'),
    path('cv_detail/<int:pk>/', CVDetail.as_view(), name='cv_detail'),
    path('', index, name='index'),
    path('', include('django.contrib.auth.urls')),
]
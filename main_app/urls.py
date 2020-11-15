from django.urls import path
from .views import (
    index,
)

app_name = 'my_app'

urlpatterns = [
    path('', index, name='index'),
]
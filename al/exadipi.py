from django.urls import path
from . import views

urlpatterns = [
    path('', views.empty_view, name='empty_view'),
]

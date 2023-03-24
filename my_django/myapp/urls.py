from django.urls import path
from . import views

urlpatterns = [
    path('', views.hello, name='hello'),
    path('members', views.testing, name='members')
]
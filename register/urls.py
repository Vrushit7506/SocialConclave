from django.urls import path,include
from .views import *
from django.views.generic import TemplateView

app_name='register'

urlpatterns = [
    path('',Registration.as_view(),name='register-page'),
]

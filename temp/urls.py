from django.urls import path
from . import views

urlpatterns = [
    path('temp/',views.template,name="template")
]
from django.urls import path
from . import views

urlpatterns = [ 
    path("", views.index),
    path("trigger", views.trigger),
    path("enable", views.enable),
    path("disable", views.disable)
]

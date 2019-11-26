"""Some"""
from django.contrib import admin
from django.urls import path
from django.http import HttpResponse

from houston import views as local_views
from measures import views as measures_views

urlpatterns = [
    path('hello-world/', local_views.hello_world),
    path('sorted/', local_views.sort_integers),
    path('hi/<str:name>/<int:age>/', local_views.say_hi),

    path('graphics/',measures_views.graphic)
]

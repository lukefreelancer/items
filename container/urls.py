from django.contrib import admin
from .models import Container
from .views import ContainerView
from rest_framework import permissions
from django.urls import include, path
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

app_name="containers"

urlpatterns = [
    path('containers/', ContainerView.as_view()),
]

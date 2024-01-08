from rest_framework.urlpatterns import format_suffix_patterns
from .views import StructureView

from django.urls import include, path

app_name="structures"

urlpatterns = [
    path('structures/', StructureView.as_view()),
]

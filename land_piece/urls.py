from rest_framework.urlpatterns import format_suffix_patterns
from .views import LandPieceView

from django.urls import include, path

app_name="land_pieces"

urlpatterns = [
    path('land_pieces/', LandPieceView.as_view()),
]

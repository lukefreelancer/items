from rest_framework.urlpatterns import format_suffix_patterns
from .views import ItemView
from django.urls import include, path


app_name="items"

urlpatterns = [
    path('items/', ItemView.as_view()),
]

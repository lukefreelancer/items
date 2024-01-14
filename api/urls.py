"""
URL configuration for api project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework.schemas import get_schema_view
from django.conf import settings
from django.conf.urls.static import static

from management.api.views import ObtainTokenView, HealthCheckView
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        #  add your swagger doc title
        title="Showroom API",
        #  version of the swagger doc
        default_version='v1',
        # first line that appears on the top of the doc
        description="Test description",
    ),
    public=True,
)


urlpatterns = [
    path("admin/", admin.site.urls),
    # Healthcheck ENDPOINT(S)
    path("api/healthcheck/", HealthCheckView.as_view(), name="healthcheck"),
    # AUTH ENDPOINT(S)
    path("api/token/", ObtainTokenView.as_view(), name="obtain_token"),
    path("api/", include("management.urls")),  # password change etc.
    path("api/management/", include("management.api.urls")),
    # application endpoints
    path('api/',include('land_piece.urls')),
    path('api/',include('structure.urls')),
    path('api/',include('container.urls')),
    path('api/',include('item.urls')),
    re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui')
]
# API Doc (open api)
# if settings.DEBUG == True:
#     urlpatterns += (
#         path(
#             "api/docs/",
#             get_schema_view(
#                 title=settings.APP_NAME,
#                 description="API Documentation",
#                 version="1.0.0",
#                 patterns=[
#                     path("api/", include("api.urls")),
#                     path("api/token/", ObtainTokenView.as_view()),
#                     path('api/',include('item.urls'))
#                 ],
#             ),
#             name="openapi-schema",
#         ),
#     )
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

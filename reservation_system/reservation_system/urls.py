from drf_spectacular.views import (
    SpectacularSwaggerView,
    SpectacularAPIView,
    SpectacularRedocView,
)

from django.contrib import admin

from django.urls import path, re_path, include
from rest_framework.authtoken import views as auth_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('reservations.urls')),
    path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
    path(
        "api/schema/swagger/",
        SpectacularSwaggerView.as_view(url_name="schema"),
        name="swagger",
    ),
    path(
        "api/schema/redoc/",
        SpectacularRedocView.as_view(url_name="schema"),
        name="redoc",
    ),
    re_path(
        r"^schema/swagger(?P<format>\.json|\.yaml)$",
        SpectacularSwaggerView.as_view(url_name="schema"),
        name="schema-json",
    ),
    path('api-token-auth/', auth_views.obtain_auth_token)
]

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView, SpectacularRedocView
import debug_toolbar

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/shop/", include("shop.urls", namespace="shop")),
    path("api/users/", include("users.urls", namespace="users")),

    path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
    path("api/doc/swagger/", SpectacularSwaggerView.as_view(url_name="schema"), name="swagger-ui"),
    path("api/doc/redoc/", SpectacularRedocView.as_view(url_name="schema"), name="redoc"),

    path("__debug__/", include(debug_toolbar.urls)),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

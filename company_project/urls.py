
from django.contrib import admin
from django.urls import path, include

from drf.api.urls import router as drf_app_router
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

urlpatterns = [
    path('admin/', admin.site.urls),
    path(r'api/', include(drf_app_router.urls)),


    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/swagger/', SpectacularSwaggerView.as_view(url_name='schema')),
]


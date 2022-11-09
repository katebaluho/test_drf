from django.urls import include, path
from rest_framework.routers import DefaultRouter

from drf.api.views.views_api import TransferViewSet

router = DefaultRouter()
router.register(r'transfer', TransferViewSet, basename='auth')

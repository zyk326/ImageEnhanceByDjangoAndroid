from rest_framework import routers
from rest_framework.routers import DefaultRouter

from .views import MerchantViewSet

urlpatterns = []

router = DefaultRouter()
router.register('merchant', MerchantViewSet, 'merchant')
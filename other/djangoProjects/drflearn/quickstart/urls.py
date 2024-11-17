from rest_framework.routers import DefaultRouter
from quickstart.views import MerchantViewset

router = DefaultRouter()
router.register('merchant', MerchantViewset, basename='merchant')

app_name = 'quickstart'
urlpatterns = [] + router.urls
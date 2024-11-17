from django.urls import path

from .views import MerchantViewSet

from .views import MerchantView

app_name = 'classview'
urlpatterns = [
    path('merchant/', MerchantView.as_view(), name='merchant'),
    path('merchant/<int:pk>/', MerchantView.as_view(), name='merchant'),
]

from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register('shangjia', MerchantViewSet, basename='shangjia')
urlpatterns += router.urls
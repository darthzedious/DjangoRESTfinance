from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import EqualInstallmentPlanViewSet


router = DefaultRouter()
router.register(r'equal_installment', EqualInstallmentPlanViewSet, basename='equal_installment')
urlpatterns = [
    path('', include(router.urls))
]
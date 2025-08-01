from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import EqualInstallmentPlanViewSet, EqualPrincipalPortionPlanViewSet, \
    EqualInstallmentChangeableIPPlanViewSet, EqualPrincipalPortionChangeableIPPlanViewSet

router = DefaultRouter()
router.register(r'equal-installment', EqualInstallmentPlanViewSet, basename='equal-installment')
router.register(r'equal-principal-portion', EqualPrincipalPortionPlanViewSet, basename='equal-principal-portion')
router.register(r'equal-installment-changeable-ip', EqualInstallmentChangeableIPPlanViewSet, basename='equal-installment-changeable-ip')
router.register(r'equal-principal-portion-changeable-ip', EqualPrincipalPortionChangeableIPPlanViewSet, basename='equal-principal-portion-changeable-ip')

urlpatterns = [
    path('', include(router.urls))
]

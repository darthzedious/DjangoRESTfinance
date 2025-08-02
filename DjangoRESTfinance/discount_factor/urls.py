from tkinter.font import names

from django.urls.conf import path

from .views import CalculateDiscountFactorView, DiscountingPresentValueView

urlpatterns = [
    path('calculate-discount-factor/', CalculateDiscountFactorView.as_view(), name='calculate-discount-factor'),
    path('discounting-present-value/', DiscountingPresentValueView.as_view(), name='discounting-present-value')
]
from django.contrib import admin
from django.urls import path, include
# from django.urls.conf import include
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('DjangoRESTfinance.accounts.urls')),
    path('repayment-plans/', include('DjangoRESTfinance.repayment_plans.urls')),
    path('annuity-factor/', include('DjangoRESTfinance.annuity_factor.urls')),
    path('discount-factor/', include('DjangoRESTfinance.discount_factor.urls')),
    # Optional UI:
    path('', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/schema/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),

]

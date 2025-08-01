from django.urls.conf import path

from .views import FvAnnuityFactorStartYear, FvAnnuityFactorEndYear, PvAnnuityStartYear,PvAnnuityEndYear

urlpatterns = [
    path('fv-annuity-factor-start-year/', FvAnnuityFactorStartYear.as_view(), name='fv-annuity-factor-start-year'),
    path('fv-annuity-factor-end-year/', FvAnnuityFactorEndYear.as_view(), name='fv-annuity-factor-end-year'),
    path('pv-annuity-factor-start-year/', PvAnnuityStartYear.as_view(), name='pv-annuity-factor-start-year'),
    path('pv-annuity-factor-end-year/', PvAnnuityEndYear.as_view(), name='pv-annuity-factor-end-year'),

]
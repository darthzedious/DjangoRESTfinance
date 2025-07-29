from django.urls.conf import path

from .views import RegisterUserView, EmailOrUsernameTokenObtainPairView, LogoutView
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path('register/', RegisterUserView.as_view(), name='register'),
    path('api/login/', EmailOrUsernameTokenObtainPairView.as_view(), name='login_token_obtain_pair'),  # LOGIN
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),  # refresh
    path('api/logout/', LogoutView.as_view(), name='logout'),
]

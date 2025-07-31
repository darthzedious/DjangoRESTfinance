from rest_framework.generics import RetrieveUpdateDestroyAPIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny, IsAuthenticated

from .models import EqualInstallmentPlan
from .serializers import EqualInstallmentPlanSerializer

class EqualInstallmentPlanViewSet(ModelViewSet):
    serializer_class = EqualInstallmentPlanSerializer
    model = EqualInstallmentPlan
    permission_classes = [IsAuthenticated]


    def get_queryset(self):
        queryset = EqualInstallmentPlan.objects.filter(user=self.request.user).order_by('-id')
        return queryset


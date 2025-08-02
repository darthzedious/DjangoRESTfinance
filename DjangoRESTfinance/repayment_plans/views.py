from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

from .models import (EqualInstallmentPlan, EqualPrincipalPortionPlan,
                     EqualInstallmentChangeableIPPlan, EqualPrincipalPortionChangeableIPPlan)
from .serializers import (EqualInstallmentPlanSerializer, EqualPrincipalPortionSerializer,
                          EqualInstallmentChangeableIPPlanSerializer, EqualPrincipalPortionChangeableIPPlanSerializer)


class EqualInstallmentPlanViewSet(ModelViewSet):
    serializer_class = EqualInstallmentPlanSerializer
    queryset = EqualInstallmentPlan.objects.all()
    permission_classes = [IsAuthenticated]


    def get_queryset(self):
        queryset = EqualInstallmentPlan.objects.filter(user=self.request.user).order_by('-id')
        return queryset


class EqualPrincipalPortionPlanViewSet(ModelViewSet):
    queryset = EqualPrincipalPortionPlan.objects.all()
    serializer_class = EqualPrincipalPortionSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = EqualPrincipalPortionPlan.objects.filter(user=self.request.user).order_by('-id')
        return queryset


class EqualInstallmentChangeableIPPlanViewSet(ModelViewSet):
    queryset = EqualInstallmentChangeableIPPlan.objects.all()
    serializer_class = EqualInstallmentChangeableIPPlanSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = EqualInstallmentChangeableIPPlan.objects.filter(user=self.request.user).order_by('id')
        return queryset


class EqualPrincipalPortionChangeableIPPlanViewSet(ModelViewSet):
    queryset = EqualPrincipalPortionChangeableIPPlan.objects.all()
    serializer_class = EqualPrincipalPortionChangeableIPPlanSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = EqualPrincipalPortionChangeableIPPlan.objects.filter(user=self.request.user).order_by('-id')
        return queryset

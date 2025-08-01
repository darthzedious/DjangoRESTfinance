from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

from .models import (EqualInstallmentPlan, EqualPrincipalPortionPlan,
                     EqualInstallmentChangeableIPPlan, EqualPrincipalPortionChangeableIPPlan)
from .serializers import (EqualInstallmentPlanSerializer, EqualPrincipalPortionSerializer,
                          EqualInstallmentChangeableIPPlanSerializer, EqualPrincipalPortionChangeableIPPlanSerializer)


class EqualInstallmentPlanViewSet(ModelViewSet):
    serializer_class = EqualInstallmentPlanSerializer
    model = EqualInstallmentPlan
    permission_classes = [IsAuthenticated]


    def get_queryset(self):
        queryset = EqualInstallmentPlan.objects.filter(user=self.request.user).order_by('-id')
        return queryset


class EqualPrincipalPortionPlanViewSet(ModelViewSet):
    model = EqualPrincipalPortionPlan
    serializer_class = EqualPrincipalPortionSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = EqualPrincipalPortionPlan.objects.filter(user=self.request.user).order_by('-id')
        return queryset


class EqualInstallmentChangeableIPPlanViewSet(ModelViewSet):
    model = EqualInstallmentChangeableIPPlan
    serializer_class = EqualInstallmentChangeableIPPlanSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = EqualInstallmentChangeableIPPlan.objects.filter(user=self.request.user).order_by('id')
        return queryset


class EqualPrincipalPortionChangeableIPPlanViewSet(ModelViewSet):
    model = EqualPrincipalPortionChangeableIPPlan
    serializer_class = EqualPrincipalPortionChangeableIPPlanSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = EqualPrincipalPortionChangeableIPPlan.objects.filter(user=self.request.user).order_by('-id')
        return queryset

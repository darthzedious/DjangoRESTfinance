from rest_framework import serializers

from .models import EqualInstallmentPlan
from .helpers import calculate_equal_installment


class EqualInstallmentPlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = EqualInstallmentPlan
        fields = '__all__'
        read_only_fields = ['user', 'created_at', 'repayment']

    def create(self, validated_data):
        repayment = calculate_equal_installment(
            validated_data['borrowed_amount'],
            validated_data['interest_rate'],
            validated_data['periods']
        )

        validated_data['repayment'] = repayment

        validated_data['user'] = self.context['request'].user
        return super().create(validated_data)

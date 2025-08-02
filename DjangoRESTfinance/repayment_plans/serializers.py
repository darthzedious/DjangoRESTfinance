from rest_framework import serializers
from drf_spectacular.utils import extend_schema_field

from .models import EqualInstallmentPlan, EqualPrincipalPortionPlan, EqualInstallmentChangeableIPPlan, EqualPrincipalPortionChangeableIPPlan
from .helpers import (calculate_equal_installment, calculate_equal_principle_portion,
                      calculate_equal_installment_changeable_ip_repayment_plan,
                      calculate_equal_principle_portion_changeable_ip_repayment_plan)


class EqualInstallmentPlanSerializer(serializers.ModelSerializer):
    user_name = serializers.SerializerMethodField()

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

    @extend_schema_field(str)
    def get_user_name(self, obj):
        return obj.user.username  # or obj.user.get_full_name() or obj.user.email


class EqualPrincipalPortionSerializer(serializers.ModelSerializer):
    user_name = serializers.SerializerMethodField()

    class Meta:
        model = EqualPrincipalPortionPlan
        fields = '__all__'
        read_only_fields = ['user', 'created_at', 'repayment']

    def create(self, validated_data):
        repayment = calculate_equal_principle_portion(
            validated_data['borrowed_amount'],
            validated_data['interest_rate'],
            validated_data['periods']
        )

        validated_data['repayment'] = repayment
        validated_data['user'] = self.context['request'].user
        return super().create(validated_data)

    @extend_schema_field(str)
    def get_user_name(self, obj):
        return obj.user.username


class EqualInstallmentChangeableIPPlanSerializer(serializers.ModelSerializer):
    user_name = serializers.SerializerMethodField()

    class Meta:
        model = EqualInstallmentChangeableIPPlan
        fields = '__all__'
        read_only_fields = ['user', 'created_at', 'repayment']

    def create(self, validated_data):
        repayment = calculate_equal_installment_changeable_ip_repayment_plan(
            validated_data['borrowed_amount'],
            validated_data['interest_rate_first_period'],
            validated_data['interest_rate_second_period'],
            validated_data['number_of_periods'],
            validated_data['second_period'],

        )

        validated_data['repayment'] = repayment
        validated_data['user'] = self.context['request'].user
        return super().create(validated_data)

    @extend_schema_field(str)
    def get_user_name(self, obj):
        return obj.user.name

class EqualPrincipalPortionChangeableIPPlanSerializer(serializers.ModelSerializer):
    user_name = serializers.SerializerMethodField()

    class Meta:
        model = EqualPrincipalPortionChangeableIPPlan
        fields = '__all__'
        read_only_fields = ['user', 'created_at', 'repayment']

    def create(self, validated_data):
        repayment = calculate_equal_principle_portion_changeable_ip_repayment_plan(
            validated_data['borrowed_amount'],
            validated_data['interest_rate_first_period'],
            validated_data['interest_rate_second_period'],
            validated_data['number_of_periods'],
            validated_data['second_period'],

        )

        validated_data['repayment'] = repayment
        validated_data['user'] = self.context['request'].user
        return super().create(validated_data)

    @extend_schema_field(str)
    def get_user_name(self, obj):
        return obj.user.name

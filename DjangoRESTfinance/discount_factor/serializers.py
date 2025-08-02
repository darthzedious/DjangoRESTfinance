from rest_framework import serializers

class BaseDiscountFactorSerializer(serializers.Serializer):
    annual_discount_rate = serializers.FloatField()
    number_of_periods = serializers.FloatField()


class CalculateDiscountFactorSerializer(BaseDiscountFactorSerializer):
    pass


class DiscountingPresentValueSerializer(BaseDiscountFactorSerializer):
    future_value = serializers.FloatField()
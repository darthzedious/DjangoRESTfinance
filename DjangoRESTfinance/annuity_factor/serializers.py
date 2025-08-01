from rest_framework import serializers

class AnnuityFactorSerializer(serializers.Serializer):
    interest_rate = serializers.FloatField()
    number_of_periods = serializers.IntegerField(min_value=1)

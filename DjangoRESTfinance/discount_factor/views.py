from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework import status

from .helpers import discounting_present_value, calculate_the_discount_factor
from .serializers import CalculateDiscountFactorSerializer, DiscountingPresentValueSerializer

class CalculateDiscountFactorView(GenericAPIView):
    serializer_class = CalculateDiscountFactorSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            annual_discount_rate = serializer.validated_data['annual_discount_rate']
            number_of_periods = serializer.validated_data['number_of_periods']

            discount_factor = calculate_the_discount_factor(annual_discount_rate, number_of_periods)
            answer = {
                'annual_discount_rate': annual_discount_rate,
                'number_of_periods': number_of_periods,
                'discount_factor': discount_factor
            }
            return Response(answer)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DiscountingPresentValueView(GenericAPIView):
    serializer_class = DiscountingPresentValueSerializer

    def post(self, request):
        serializer = DiscountingPresentValueSerializer(data=request.data)
        if serializer.is_valid():
            future_value = serializer.validated_data['future_value']
            annual_discount_rate = serializer.validated_data['annual_discount_rate']
            number_of_periods = serializer.validated_data['number_of_periods']

            discounted_present_value = discounting_present_value(fv=future_value, r=annual_discount_rate, n=number_of_periods)
            answer = {
                'future_value': future_value,
                'annual_discount_rate': annual_discount_rate,
                'number_of_periods': number_of_periods,
                'discounted_present_value': discounted_present_value,
            }
            return Response(answer)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
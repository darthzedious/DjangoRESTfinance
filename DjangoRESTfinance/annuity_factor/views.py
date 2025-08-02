from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import GenericAPIView
from drf_spectacular.utils import extend_schema

from .serializers import AnnuityFactorSerializer
from .helpers import (calculate_future_value_annuity_factor_end_year_payment,
                      calculate_future_value_annuity_factor_start_year_payment,
                      calculate_present_value_annuity_factor_start_year_payment,
                      calculate_present_value_annuity_factor_end_year_payment,
                      )

class FvAnnuityFactorStartYear(APIView):

    @extend_schema(request=AnnuityFactorSerializer)
    def post(self, request):
        serializer = AnnuityFactorSerializer(data=request.data)
        if serializer.is_valid():
            interest_rate = serializer.validated_data['interest_rate']
            number_or_periods = serializer.validated_data['number_of_periods']

            annuity_factor = calculate_future_value_annuity_factor_start_year_payment(interest_rate, number_or_periods)
            answer = {
                "interest_rate": interest_rate,
                "number-of_periods": number_or_periods,
                "Future Value Annuity Factor Start year payment": annuity_factor,
            }

            return Response(answer)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# without the decorator
class FvAnnuityFactorEndYear(GenericAPIView):
    serializer_class = AnnuityFactorSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            interest_rate = serializer.validated_data['interest_rate']
            number_or_periods = serializer.validated_data['number_of_periods']

            annuity_factor = calculate_future_value_annuity_factor_end_year_payment(interest_rate, number_or_periods)
            answer = {
                "interest_rate": interest_rate,
                "number-of_periods": number_or_periods,
                "Future Value Annuity Factor End year payment": annuity_factor,
            }
            return Response(answer)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PvAnnuityStartYear(APIView):

    @extend_schema(request=AnnuityFactorSerializer)
    def post(self, request):
        serializer = AnnuityFactorSerializer(data=request.data)
        if serializer.is_valid():
            interest_rate = serializer.validated_data['interest_rate']
            number_of_periods = serializer.validated_data['number_of_periods']

            annuity_factor = calculate_present_value_annuity_factor_start_year_payment(interest_rate, number_of_periods)
            answer = {
                'interest_rate': interest_rate,
                'number_of_periods': number_of_periods,
                'annuity_factor': annuity_factor
            }
            return Response(answer)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PvAnnuityEndYear(GenericAPIView):
    serializer_class = AnnuityFactorSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            interest_rate = serializer.validated_data['interest_rate']
            number_of_periods = serializer.validated_data['number_of_periods']

            annuity_factor = calculate_present_value_annuity_factor_end_year_payment(interest_rate, number_of_periods)
            answer = {
                'interest_rate': interest_rate,
                'number_of_periods': number_of_periods,
                'annuity_factor': annuity_factor
            }
            return Response(answer)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

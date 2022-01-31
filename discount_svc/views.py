from rest_framework import viewsets, status
from rest_framework.response import Response
from discount_svc.serializers import DiscountCodeCreateSerializer
from discount_svc.discount_code import create_discount_codes, retrieve_and_assign_code


class DiscountCodeBrandViewSet(viewsets.ViewSet):
    def batch_create(self, request, brand_id, campaign_id):
        serializer = DiscountCodeCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        response_body = create_discount_codes(brand_id, campaign_id, serializer.data)
        return Response(response_body, status=status.HTTP_201_CREATED)


class DiscountCodeCustomerViewSet(viewsets.ViewSet):
    def retrieve_and_assign(self, request, customer_id, campaign_id):
        response_body = retrieve_and_assign_code(customer_id, campaign_id)
        if response_body:
            return Response(response_body, status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)

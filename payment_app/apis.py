from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated


from payment_app.gateway_handlers import RazorpayPaymentHandler

class CreateSubOrderAPI(APIView):

    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        data = request.data
        data['user_id'] = request.user.id

        resp = RazorpayPaymentHandler.create_sub_order(**data)

        return Response(
            resp, 
            status=status.HTTP_201_CREATED
        )

class AcceptSubPayment(APIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,) 

    def post(self, request, *args, **kwargs):

        order_id = request.query_params.get('order_id')
        resp = RazorpayPaymentHandler.handle_sub_order_payment(order_id)

        return Response(
            resp,
            status=status.HTTP_200_OK
        )

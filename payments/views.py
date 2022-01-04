from rest_framework.permissions import AllowAny
import stripe
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


stripe.api_key ='sk_test_51KDMRRSJ2WdoqlsxXqYNq4lB91mtGOGG4nLna4rzsGFHx2nhPxJIK9ChPX2Z5O6yNIP5aVSbUOFoQY7PaqMUndmz00OtzhrOJD'


class OrderPlace(APIView):
    permission_classes = [AllowAny]
    def post(self, request, format='json'):
        payment_intent = request.data['payment_intent']
        payment_status = stripe.PaymentIntent.retrieve(payment_intent)
        print(payment_status)
        if(payment_status.status == 'succeeded'):
            return Response(status=status.HTTP_200_OK, data={'order':'success'})
        return Response(status=status.HTTP_400_OK, data={'order':'fail'})


class MakePayment(APIView):
    permission_classes = [AllowAny]
    def post(self, request, format='json'):
        data = request.data
        # print(data)
        intent = stripe.PaymentIntent.create(
            amount=100000,
            currency='inr',
            automatic_payment_methods={
                'enabled': True,
            },
        )
        return Response(status=status.HTTP_200_OK, data={'clientSecret': intent['client_secret']})

class saveStripeInfo(APIView):
    permission_classes = [AllowAny]
    def post(self, request, format='json'):
        data = request.data
        email = data['email']
        payment_method_id = data['payment_method_id']
        amount = data['amount']
        extra_msg = '' # add new variable to response message
        # checking if customer with provided email already exists
        customer_data = stripe.Customer.list(email=email).data   
        
        # if the array is empty it means the email has not been used yet  
        if len(customer_data) == 0:
            # creating customer
            customer = stripe.Customer.create(
            email=email, payment_method=payment_method_id)
        else:
            customer = customer_data[0]
            extra_msg = "Customer already existed."
        stripe_res = stripe.PaymentIntent.create(
            customer=customer, 
            payment_method=payment_method_id,  
            currency='inr',
            amount=amount)
        confirm = stripe.PaymentIntent.confirm(stripe_res)
        return Response(status=status.HTTP_200_OK, 
            data={'message': 'success', 'data': {
            'customer_id': customer.id, 'extra_msg': extra_msg ,'confirm_url': confirm.next_action.use_stripe_sdk.stripe_js}
            })
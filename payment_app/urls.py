from django.urls import path
from payment_app.apis import CreateSubOrderAPI, AcceptSubPayment


urlpatterns = [
    path('sub/create/', CreateSubOrderAPI.as_view(), name='create_sub_order'),
    path('sub/accept/', AcceptSubPayment.as_view(), name='accept_sub_payment'),
]


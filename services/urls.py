from django.urls import path
from .views import services, index, payment_user, expired_payments

urlpatterns = [
    path('services/', services, name = 'servicios'),
    path('payment_user/', payment_user, name = 'payment_user'),
    path('expired_payments/', expired_payments, name = 'expired_payments'),
    path('', index, name = 'index')
]
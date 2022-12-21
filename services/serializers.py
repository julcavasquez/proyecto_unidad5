from rest_framework import serializers
from .models import Services, Payment_user, Expired_payments

class ServicesSerializador(serializers.ModelSerializer):
    class Meta:
        model = Services
        fields = ('name','description','logo')

class PaymentUserSerializador(serializers.ModelSerializer):
    class Meta:
        model = Payment_user
        fields = ('amount','paymentDate','expirationDate')

class ExpiredPaymentsSerializador(serializers.ModelSerializer):
    class Meta:
        model = Payment_user
        fields = ('penalty_fee_amount')
from django.db import models
from users.models import User
# Create your models here.


class Services(models.Model):
    name = models.CharField(max_length=50) 
    description = models.CharField(max_length=150)
    logo = models.CharField(max_length=200)

    def __str__(self) -> str:
        return self.name

    class Meta:
        db_table='services'


class Payment_user(models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(User,on_delete=models.CASCADE, null=True)
    service_id = models.ForeignKey(Services,on_delete=models.CASCADE, null=True)
    amount = models.FloatField(default=0.0)
    paymentDate = models.DateField(auto_now_add=True)
    expirationDate = models.DateField(auto_now_add=True)

    class Meta:
        db_table='payment_user'


class Expired_payments(models.Model):
    id = models.AutoField(primary_key=True)
    payment_user_id = models.ForeignKey(Payment_user,on_delete=models.CASCADE, null=True)
    penalty_fee_amount = models.FloatField(default=0.0)
    
    class Meta:
        db_table='expired_payments'
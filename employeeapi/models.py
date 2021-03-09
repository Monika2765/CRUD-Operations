from django.db import models

# Create your models here.
class Customer(models.Model):
    user_id=models.CharField(max_length=15)
    amount=models.CharField(max_length=10)
    coins_balance=models.CharField(max_length=10)
    txn_type=models.CharField(max_length=10)
    txn_info=models.CharField(max_length=10)
    action=models.CharField(max_length=10)
    time=models.CharField(max_length=13)
    
    
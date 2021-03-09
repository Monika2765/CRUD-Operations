from django import forms
from .models import Customer

class CustomerForm(forms.ModelForm):
     
     class Meta:
         model=Customer
         fields='__all__'
         labels={
             'user_id':'User Id',
             'amount':'Amount',
             'coins_balance':'Coins Balance',
             'txn_type':'Txn-Type',
             'txn_info':'Txn-Info',
             'action':'Action',
             'time':'Time'
         }
         
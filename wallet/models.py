from datetime import datetime, timezone
from symtable import Symbol
from django.db import models

# Create your models here.
class Customers(models.Model):
    first_name=models.CharField(max_length=15)
    last_name=models.CharField(max_length=15)
    gender= models.CharField(max_length=10)
    address=models.TextField(max_length=15)
    age=models.PositiveSmallIntegerField()
    nationality=models.CharField(max_length=15)
    id_number=models.CharField(max_length=10)
    email=models.EmailField()
    phone_number=models.CharField(max_length=15)

class Wallet(models.Model):
        balance = models.IntegerField()
        date = models.DateTimeField(default=datetime.now)
        is_active = models.BooleanField(default=False)
        currency = models.CharField(max_length=10)
        profile = models.ImageField(upload_to='profile/',null=True)
        customer = models.ForeignKey(Customers,on_delete=models.CASCADE,related_name='Wallet_customer')
        pin = models.SmallIntegerField()
        type =models.CharField(max_length=15,null=True)
        
        
class Account(models.Model):
        wallet = models.ForeignKey(Wallet,on_delete=models.CASCADE,related_name='Account_wallet')
        account_type = models.CharField(max_length=15,null=True)
        balance = models.IntegerField()
        name = models.CharField(max_length=50,null=True)
        
           
class Transaction (models.Model):
        amount = models.IntegerField()
        thirdparty = models.ForeignKey('Thirdparty',on_delete=models.CASCADE,related_name='Transaction_thirdparty')
        status = models.CharField(max_length=15,null=True)
        account_origin =  models.ForeignKey(Account,on_delete=models.CASCADE,related_name='Transaction_account_origin')
        destination = models.ForeignKey(Account,on_delete=models.CASCADE,related_name='Transaction_destination')
        receipt = models.CharField(max_length=20,null=True)
             
class Card(models.Model):
        date_issued = models.DateTimeField(default=datetime.now)
        CVV_security_code = models.PositiveSmallIntegerField()
        signature = models.ImageField(upload_to='profile/',null=True)
        card_status = models.CharField(max_length=100,null=True)
        account = models.ForeignKey(Account,on_delete=models.CASCADE,related_name='Card_Account')
        
class Thirdparty(models.Model):
        email = models.EmailField()
        phone_number = models.CharField(max_length=10,null=True)
        transaction_cost = models.IntegerField()
        currency = models.ForeignKey('Currency',on_delete=models.CASCADE,related_name='Thirdparty_currency')
        account = models.ForeignKey(Account,on_delete=models.CASCADE,related_name='Thirdparty_account')
        is_active = models.BooleanField(default=False)
        
class Notification(models.Model):
        message = models.CharField(max_length=200,null=True)
        data_created = models.DateTimeField(default=datetime.now)
        is_active = models. BooleanField(default=False)
        receipt =  models.ForeignKey('Receipt',on_delete=models.CASCADE,related_name='Notification_receipt')
        message = models.CharField(max_length=200,null=True)
        image = models.ImageField(upload_to='profile/',null=True)
        
class Receipt(models.Model):
        receipt = models.DateTimeField(default=datetime.now)
        transaction = models.ForeignKey(Transaction,on_delete=models.CASCADE,related_name='Reciept_transaction')
        file = models.FileField()
        date = models.DateTimeField(default=datetime.now)
        receipt_file = models.FileField()
    
class Loan (models.Model):
        amount = models.PositiveIntegerField()
        duration_in_month = models.CharField(max_length=12,null=True)
        status = models.CharField(max_length=40,null=True)
        wallet = models.ForeignKey(Wallet,on_delete=models.CASCADE,related_name='Loan_wallet')
        date_time = models.DateTimeField(default=datetime.now)
        interest_rate = models.IntegerField()
        balance = models.IntegerField()
        guaranter = models.CharField(max_length=15,null=True)
        
class Reward (models.Model):    
        wallet = models.ForeignKey(Wallet,on_delete=models.CASCADE,related_name='Reward_wallet')
        name = models.CharField(max_length=15,null=True)
        points = models.IntegerField()
        date = models.DateTimeField(default=datetime.now)
        transation = models.ForeignKey('Transaction',on_delete=models.CASCADE,related_name='Reward_transaction')
    
class currency(models.Model):
    Symbol=models.CharField(max_length=10,null=True)
    name=models.CharField(max_length=15,null=True)
    country=models.CharField(max_length=15,null=True)

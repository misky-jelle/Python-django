from django.contrib import admin

from .models import Customers,Wallet,Account,Transaction,Card,Thirdparty,Notification,Receipt,Loan,Reward,currency

# Register your models here.
class CustomerAdmin(admin.ModelAdmin):
    list_display = ("first_name","last_name","email")
    search_fields = ("first_name","last_name")
    
admin.site.register(Customers,CustomerAdmin)
admin.site.register(Wallet)
admin.site.register(Account)
admin.site.register(Transaction)
admin.site.register(Card)
admin.site.register(Thirdparty)
admin.site.register(Notification)
admin.site.register(Receipt)
admin.site.register(Loan)
admin.site.register(Reward)
admin.site.register(currency)
from django.contrib import admin
from .models  import User,Wallet,Currency,Transaction,Card,Notifications,Receipts,ThirdParty,Receipts,Loan


class UserAdmin(admin.ModelAdmin):
    list_display = ('email', 'firstName', 'lastName', 'age',)
    search_fields = ('email', 'firstName', 'lastName', 'age',)

# Register your models here.
admin.site.register(User, UserAdmin)
admin.site.register(Wallet)
admin.site.register(Currency)
admin.site.register(Transaction)
admin.site.register(Receipts)
admin.site.register(ThirdParty)
admin.site.register(Notifications)
admin.site.register(Card)
admin.site.register(Loan)


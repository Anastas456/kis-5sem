from django.contrib import admin
from .models import Currency, Payment


class CurrencyAdmin(admin.ModelAdmin):
    list_display = ('code', 'name', 'rate')
    list_filter = ('code', 'name', 'rate')
    search_fields = ('code', 'name', 'rate')

class PaymentAdmin(admin.ModelAdmin):
    list_display = ('id', 'payment_date', 'organization', 'contract', 'amount_in_rubles', 'currency')
    list_filter = ('id', 'organization', 'contract')
    search_fields = ('id', 'payment_date', 'organization', 'contract')


admin.site.register(Currency, CurrencyAdmin)
admin.site.register(Payment, PaymentAdmin)

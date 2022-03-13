from django.contrib import admin
from .models import Client, Russian_passport, International_passport


class ClientAdmin(admin.ModelAdmin):
    list_display = ('id', 'status', 'surname', 'name', 'patronymic')
    list_filter = ('id', 'status', 'surname', 'name', 'sex')
    search_fields =('id', 'status', 'surname', 'name', 'sex', 'date_of_birth')


class RussianPassportAdmin(admin.ModelAdmin):
    list_display = ('id', 'client')
    list_filter = ('id', 'client')
    search_fields = ('id', 'client', 'passport_series', 'passport_number', 'date_of_issue', 'expiration_date')


class InternationalPassportAdmin(admin.ModelAdmin):
    list_display = ('id', 'client', 'country_code')
    list_filter = ('id', 'client', 'country_code')
    search_fields = ('id', 'client', 'country_code', 'passport_number', 'issuing_authority', 'date_of_issue', 'expiration_date')


admin.site.register(Client, ClientAdmin)
admin.site.register(Russian_passport, RussianPassportAdmin)
admin.site.register(International_passport, InternationalPassportAdmin)
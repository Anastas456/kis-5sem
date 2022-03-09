from django.contrib import admin
from .models import Employee, Organization


class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('id', 'surname', 'name', 'patronymic', 'position')
    list_filter = ('id', 'surname', 'position')
    search_fields = ('id', 'surname', 'position')

class OrganizationAdmin(admin.ModelAdmin):
    list_display = ('id', 'organization_name')
    list_filter = ('id', 'organization_name')
    search_fields = ('id', 'organization_name')


admin.site.register(Employee, EmployeeAdmin)
admin.site.register(Organization, OrganizationAdmin)

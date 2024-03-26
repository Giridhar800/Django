from django.contrib import admin
from querysetapi.models import Employee

# Register your models here.
@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'eid', 'eaddress', 'age', 'dob']

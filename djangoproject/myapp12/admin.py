from django.contrib import admin
from myapp12.models import customer

# Register your models here.
@admin.register(customer)
class customerAdmin(admin.ModelAdmin):
    list_display = ['name', 'address', 'mailid']

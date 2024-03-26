from django.contrib import admin
from myapp10.models import Students


# Register your models here.
@admin.register(Students)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['name', 'mailid', 'address', 'password']

from django.contrib import admin
from editingview.models import StudentModel

# Register your models here.
@admin.register(StudentModel)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['name', 'mail', 'msg']

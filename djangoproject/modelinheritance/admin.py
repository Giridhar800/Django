from django.contrib import admin
from modelinheritance.models import Teacher, Trainer, Bank, BankManager, University, College


# Register your models here.
@admin.register(Trainer)
class TrainerModel(admin.ModelAdmin):
    list_display = ['id', 'name', 'age', 'address']

@admin.register(Teacher)
class TeacherModel(admin.ModelAdmin):
    list_display = ['id', 'name', 'date', 'salary']

@admin.register(Bank)
class BankAdmin(admin.ModelAdmin):
    list_display = ['id', 'bname', 'baddress']

@admin.register(BankManager)
class BankManagerAdmin(admin.ModelAdmin):
    list_display = ['id', 'bname', 'baddress', 'name', 'age']

@admin.register(University)
class UniversityAdmin(admin.ModelAdmin):
    list_display = ['id', 'uname', 'ulocation']

@admin.register(College)
class CollegeAdmin(admin.ModelAdmin):
    list_display = ['id', 'uname', 'ulocation']

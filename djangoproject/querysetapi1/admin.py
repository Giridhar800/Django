from django.contrib import admin
from querysetapi1.models import Employee, Manager, Student


# Register your models here.
@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'eid', 'eaddress', 'age', 'dob']

@admin.register(Manager)
class ManagerAdmin(admin.ModelAdmin):
    list_display =['id', 'mname', 'eaddress', 'salary', 'dob']

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display =['id', 'name', 'sid', 'address', 'marks', 'passdate', 'admitdate']

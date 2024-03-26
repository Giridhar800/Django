from django.shortcuts import render
from querysetapi.models import Employee

# Create your views here.
def v1(request):
    employee_data = Employee.objects.all()
    # employee_data = Employee.objects.filter(eaddress='kurnool')
    # employee_data = Employee.objects.exclude(eaddress='kurnool')
    # employee_data = Employee.objects.order_by('?')
    # employee_data = Employee.objects.order_by('eid').reverse()[1:3]
    # employee_data = Employee.objects.values_list('id', 'name', named=True)
    # employee_data = Employee.objects.using('default')
    # employee_data = Employee.dates('dob', 'month')
    print('return type:', employee_data)
    print('SQL query:', employee_data.query)
    return render(request, "display.html", {'Employees': employee_data})

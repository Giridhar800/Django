from django.shortcuts import render
from querysetapi1.models import Employee, Manager, Student
from django.db.models import Q
from datetime import date, time
from django.db.models import Avg, Sum, Min, Max, Count

# Create your views here.
# def v1(request):
#     employee_data = Employee.objects.none()
#     qs1 = Employee.objects.values_list('id', 'name', named=True)
#     qs2 = Manager.objects.values_list('id', 'mname', named=True)
    # employee_data = qs2.union(qs1, all=True)
    # employee_data = qs2.intersection(qs1)
    # employee_data = qs2.difference(qs1)
    # employee_data = Employee.objects.filter(id=1) & Employee.objects.filter(age=23)
    # employee_data = Employee.objects.filter(Q(id=1, age=24))
    # employee_data = Employee.objects.filter(Q(id=2) | Q(age=23))
    # print("return type:", employee_data)
    # print("SQL query:", employee_data.query)
    # return render(request, 'display1.html', {'Employees': employee_data})

def home(request):
    student_data = Student.objects.all()
    # student_data = Student.objects.filter(name__iexact='GIRI')
    # student_data = Student.objects.filter(name__contains='s')
    # student_data = Student.objects.filter(name__icontains='V')
    # student_data = Student.objects.filter(marks__in=[80])
    average = student_data.aggregate(Avg('marks'))
    total = student_data.aggregate(Sum('marks'))
    minimum = student_data.aggregate(Min('marks'))
    maximum = student_data.aggregate(Max('marks'))
    totalcount =student_data.aggregate(Count("marks"))
    context = {'students':student_data, 'average':average, 'total':total, 'minimum':minimum, 'maximum':maximum, 'totalcount':totalcount}

    print(average)
    print("return:", student_data)
    print("SQL Query:", student_data.query)
    return render(request, 'display1.html', context)
from django.shortcuts import render
from myapp12.forms import customerModel
from django.contrib import messages
# Create your views here.

# def home(request):
#     return render(request, "h27.html")
#
# def emp_details(request,emp_id):
#     if emp_id == 1:
#         emp = {'id': emp_id,'name': "giri"}
#     if emp_id == 2:
#         emp = {'id': emp_id,'name': "venkey"}
#     if emp_id == 3:
#         emp = {'id': emp_id,'name': "sunil"}
#     if emp_id == 4:
#         emp = {'id': emp_id,'name': "hari"}
#     return render(request, 'h26.html', emp)
def msg(request):
    if request.method == 'POST':
        form = customerModel(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, "record sucussfly recorded")
            messages.info(request, "Inserted, now you can check in data base")
    else:
        form = customerModel()
    return render(request, 'h28.html', {'form': form})
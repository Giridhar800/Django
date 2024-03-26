from django.shortcuts import render
from editingview.models import StudentModel
from django.views.generic.edit import CreateView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView
from django.views.generic.base import TemplateView

# Create your views here.
class StudentModelView(CreateView):
    model = StudentModel
    template_name = "student.html"
    fields = ['name', 'mail', 'msg']
    success_url = '/success/'
class StudentUpdateView(UpdateView):
    model = StudentModel
    template_name = "student.html"
    fields = ['name', 'mail', 'msg']
    success_url = '/success/'

class StudentDeleteView(DeleteView):
    model = StudentModel
    template_name = "student.html"
    fields = ['name', 'mail', 'msg']
    success_url = '/success/'


class SuccessTemplateView(TemplateView):
    template_name = "success.html"

class NoDeleteView(TemplateView):
    template_name = "nodelete.html"
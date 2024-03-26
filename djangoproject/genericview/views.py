from django.shortcuts import render
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from genericview.models import Student1

# Create your views here.
class StudentDetailsView(DetailView):
    model = Student1
    template_name = 'student_details.html'
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['all_student'] = self.model.objects.all()
        return context
class StudentListView(ListView):
    model = Student1
    template_name = 'student_list.html'


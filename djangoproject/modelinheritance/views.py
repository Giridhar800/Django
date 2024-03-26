from django.shortcuts import render
from modelinheritance.models import Teacher, Trainer


# Create your views here.
def display(request):
    trainer_data = Trainer.objects.all()
    teacher_data = Teacher.objects.all()
    return render(request, 'display1.html', {'trainers':trainer_data, 'teachers': teacher_data})
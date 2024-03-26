from django.shortcuts import render, HttpResponse
from django.views.generic import View, TemplateView, RedirectView
from baseview.forms import MyForm

# Create your views here.
def fun_view(request, template_name):
    temp = template_name
    context = {'msg': 'This is giri creation'}
    return render(request, temp, context)


class class_view(View):
    template_name = ''
    def get(self, request):
        context = {'msg': "this is giri creation"}
        return render(request, self.template_name, context)

class MyTemplateView(TemplateView):
    template_name = 'home.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['name'] = "Giridhar"
        context['mail'] = 'giri@gmail.com'
        return context

class flipkart(RedirectView):
    url = 'https://flipkart.com'

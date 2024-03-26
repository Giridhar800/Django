from django import forms
class StudentForms(forms.Form):

    name = forms.CharField()
    job = forms.CharField()
    salary = forms.IntegerField()
    adress = forms.CharField()
    email = forms.EmailField()
    discription = forms.CharField()


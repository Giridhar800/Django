from django import forms
class MyForm(forms.Form):
    name = forms.CharField(max_length=20)
    address = forms.CharField(max_length=30)
from django import forms
class StudentForm(forms.Form):
    name = forms.CharField(max_length=20)
    mailid = forms.EmailField(max_length=30)
    address = forms.CharField(max_length=20)
    password = forms.CharField(widget=forms.PasswordInput)
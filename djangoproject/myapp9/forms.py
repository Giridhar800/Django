from django import forms
from django.core import validators


def starts_with_s(v):
    if v[0] != "s":
        raise forms.ValidationError("name must be start with s")

class StudentForm(forms.Form):
    name = forms.CharField(validators=[starts_with_s])

    marks = forms.IntegerField()
    password = forms.CharField(widget=forms.PasswordInput)
    rpassword = forms.CharField(widget=forms.PasswordInput)
    # def clean(self):
    #     super().clean()
    #     pwd = self.cleaned_data["password"]
    #     rpwd = self.cleaned_data["rpassword"]
    #     if pwd != rpwd:
    #         raise forms.ValidationError("pass miss match")


    # def clean_name(self):
    #     name = self.cleaned_data["name"]
    #     if len(name) < 6:
    #         raise forms.ValidationError("enter more than 6")
    #     return name


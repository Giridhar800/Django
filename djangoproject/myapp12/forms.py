from django import forms
from myapp12.models import customer

class customerModel(forms.ModelForm):
    class Meta:
        model = customer
        fields = '__all__'

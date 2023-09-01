from django import forms
from app.models import MyModel

class MyForm(forms.ModelForm):
    class Meta:
        model = MyModel
        fields = ['field1', 'field2', 'field3']


from django import forms
from app.models import MyModel

class MyForm(forms.ModelForm): 
    
    class Meta:
        model = MyModel
        fields = ['field1','field2', 'field3']
        
        widgets = {
            'field1': forms.TextInput(attrs={
                'class' : 'form-control'
            }),
            
            'field2' : forms.TextInput(attrs ={
                'class' : 'form-control',
                'label' : 'Field 2 (Integer Only)'
            }),
            
            'field3': forms.CheckboxInput(attrs = {
                'class' : 'form-check-input'
            })
        }
        


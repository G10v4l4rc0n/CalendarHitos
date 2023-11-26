from django import forms
from .models import Hito


class DateTimeInput(forms.DateTimeInput):
    input_type = 'datetime-local'

class HitoForm(forms.ModelForm):
    class Meta:
        model = Hito
        fields = '__all__'
        widgets = {
            'fecha': DateTimeInput(attrs={'class': 'form-control'}),
            'hora_inicio': DateTimeInput(attrs={'class':'form-control'}),
            'hora_fin': DateTimeInput(attrs={'class':'form-control'}),
            'todo_el_dia': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }
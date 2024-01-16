from django import forms 
from .models import Tasks
class TaskRegistration(forms.ModelForm):
    class Meta:
        model = Tasks
        fields=['task','start_time','end_time']
        widgets={
            'task':forms.TextInput(attrs={'class':'form-control'}),
            'start_time':forms.TimeInput(attrs={'class':'form-control'}),
            'end_time':forms.TimeInput(attrs={'class':'form-control'}),
        }
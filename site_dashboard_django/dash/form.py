from django import forms 
from django.utils.translation import gettext_lazy as _


class ProjectForm(forms.Form):
    

    name = forms.CharField(label="nom du projet", widget=forms.TextInput(attrs={'class': 'w-full rounded-lg h-8 border-1 border-green-400'}))
    start_date = forms.DateTimeField(required=False, widget=forms.DateInput(
        format=('%Y-%m-%d'),
        attrs={'class': 'form-control rounded-lg h-8 border-1 border-green-400 w-full', 
               'placeholder': 'Select a date',
               'type': 'date'
              }),)
    end_date = forms.DateTimeField(required=False, widget=forms.DateInput(
        format=('%Y-%m-%d'),
        attrs={'class': 'form-control rounded-lg h-8 border-1 border-green-400 w-full', 
               'placeholder': 'Select a date',
               'type': 'date'
              }),)
    
        
    DEMO_CHOICES =(
        ("N", "Nouveau"),
        ("I", "En cours"),
        ("S", "Suspendu"),

    )

    status = forms.MultipleChoiceField(required=False, choices = DEMO_CHOICES)
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
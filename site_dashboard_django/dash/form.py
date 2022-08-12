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
        ("S", "Suspendu"),)
    status = forms.MultipleChoiceField(required=False, choices = DEMO_CHOICES, widget=forms.SelectMultiple(
        attrs={'class':"bg-gray-50 border border-green-400 text-gray-900 text-sm rounded-lg focus:ring-green-500 focus:border-green-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-green-500 dark:focus:border-green-500"}
    ))  
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class UsForm(forms.Form):
    name = forms.CharField(label="nom du l'US", widget=forms.TextInput(attrs={'class': 'w-full rounded-lg h-8 border-1 border-green-400'}))
    i_want = forms.CharField(label="Je veux", widget=forms.TextInput(attrs={'class': 'w-full rounded-lg h-8 border-1 border-green-400'}))
    
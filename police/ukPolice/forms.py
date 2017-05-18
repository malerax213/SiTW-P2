from django import forms
from django.contrib.auth.models import User
from django.forms import ModelForm
from models	import Crime, Outcome, NeighbourhoodPriority


class SignUpForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password', 'email', 'first_name', 'last_name']
        widgets = {
            'password': forms.PasswordInput(),
        }

class CrimeForm(ModelForm):
    class Meta:
        model = Crime
        exclude = ('user', 'date',)

class OutcomeForm(ModelForm):
    class Meta:
        model = Outcome
        exclude = ('user', 'date',)

class NeighbourhoodPriorityForm(ModelForm):
    class Meta:
        model = NeighbourhoodPriority
        exclude = ('user', 'date',)

# knowledgebase/forms.py
from django import forms
from .models import Registration

class R_f(forms.ModelForm):
    class Meta:
        model = Registration
        fields = ['name', 'email']  # Include only the fields present in the model

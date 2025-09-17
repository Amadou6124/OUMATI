from dataclasses import field
from django import forms
from .models import ContactForm


class ContactMessage(forms.ModelForm):
    class Meta:
        model = ContactForm
        fields = ['nom', 'email', 'sujet', 'message']
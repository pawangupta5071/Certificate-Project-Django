# cert_app/forms.py
from django import forms
from .models import Certificate

class CertificateForm(forms.ModelForm):
    class Meta:
        model = Certificate
        fields = ['teacher', 'student', 'text']

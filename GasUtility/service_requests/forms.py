from django import forms
from .models import ServiceRequest

class ServiceRequestForm(forms.ModelForm):
    class Meta:
        model = ServiceRequest
        fields = ['request_type', 'description', 'attachment']
        widgets = {
            'request_type': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter request type'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Describe your issue'}),
            'attachment': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }
        labels = {
            'request_type': 'Request Type',
            'description': 'Description',
            'attachment': 'Attach a file (optional)',
        }

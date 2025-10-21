from django import forms
from .models import Customer
from .models import Worker

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['name', 'phone', 'email', 'address']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Full Name'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Phone Number'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email Address'}),
            'address': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Address'}),
        }

class WorkerForm(forms.ModelForm):
    class Meta:
        model = Worker
        fields = ['name', 'role', 'phone']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Worker Name'}),
            'role': forms.Select(attrs={'class': 'form-select'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Phone Number'}),
        }

from .models import Estimate

class EstimateForm(forms.ModelForm):
    class Meta:
        model = Estimate
        fields = ['customer', 'outline', 'detailed_description', 'visit_date', 'amount', 'status']
        widgets = {
            'customer': forms.Select(attrs={'class': 'form-select'}),
            'outline': forms.Textarea(attrs={'class': 'form-control', 'rows': 2, 'placeholder': 'Brief outline of proposed work'}),
            'detailed_description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Detailed work description'}),
            'visit_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'amount': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Estimated cost (KSh)'}),
            'status': forms.Select(attrs={'class': 'form-select'}),
        }

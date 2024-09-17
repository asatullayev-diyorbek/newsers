from django import forms
from .models import Email

class EmailForm(forms.ModelForm):
    email = forms.EmailField(
        max_length=255,
        widget=forms.EmailInput(attrs={
            'class': 'form-control w-100 py-3 rounded-pill',
            'placeholder': 'Obuna uchun e-mail'
        })
    )

    class Meta:
        model = Email
        fields = ['email']


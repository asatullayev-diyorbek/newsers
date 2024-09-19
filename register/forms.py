from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from django.contrib.auth import authenticate


class RegisterForm(forms.Form):
    first_name = forms.CharField(
        max_length=30, required=True,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
            }
        )
    )
    last_name = forms.CharField(
        max_length=30, required=True,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
            }
        )
    )
    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(
            attrs={
                'class': 'form-control',
            }
        )
    )
    username = forms.CharField(
        max_length=15, required=True,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
            }
        )
    )
    password1 = forms.CharField(
        max_length=30, required=True,
        min_length=6,
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
            }
        )
    )
    password2 = forms.CharField(
        max_length=30, required=True,
        min_length=6,
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
            }
        )
    )

    # Email unique bo'lishi kerak
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise ValidationError("Bu email allaqachon ro'yxatdan o'tgan.")
        return email

    # Username unique bo'lishi kerak
    def clean_username(self):
        username = self.cleaned_data.get('username')
        if User.objects.filter(username=username).exists():
            raise ValidationError("Bu username allaqachon band qilingan.")
        return username

    # Parollar bir-biriga mos kelishini tekshirish
    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get('password1')
        password2 = cleaned_data.get('password2')

        if password1 and password2 and password1 != password2:
            raise ValidationError("Parollar mos emas.")

        return cleaned_data


class LoginForm(forms.Form):
    username = forms.CharField(
        max_length=30, required=True,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    password = forms.CharField(
        required=True,
        widget=forms.PasswordInput(attrs={'class': 'form-control'})
    )

    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get('username')
        password = cleaned_data.get('password')

        if username and password:
            user = authenticate(username=username, password=password)
            if not user:
                raise ValidationError("Foydalanuvchi nomi yoki parol noto‘g‘ri.")
            cleaned_data['user'] = user
        return cleaned_data

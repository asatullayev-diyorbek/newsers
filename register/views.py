from django.contrib.auth import login, logout
from django.contrib.auth.hashers import make_password
from django.contrib import messages
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib.auth.models import User

from .forms import RegisterForm, LoginForm
from .models import UserConfirmation


class RegisterView(View):
    def get(self, request):
        form = RegisterForm()

        context = {
            'form': form,
            'title': "Ro'yxatdan o'tish"
        }
        return render(request, 'register/register.html', context)

    def post(self, request):
        form = RegisterForm(request.POST)
        if form.is_valid():
            User.objects.create(
                username=form.cleaned_data['username'],
                password=make_password(form.cleaned_data['password1']),
                first_name=form.cleaned_data['first_name'],
                last_name=form.cleaned_data['last_name'],
                email=form.cleaned_data['email'],
                is_active=False,
                is_staff=False,
            )
            confirmation_code = UserConfirmation.generate_confirmation_code()
            UserConfirmation.objects.create(
                user=User.objects.get(username=form.cleaned_data['username']),
                confirmation_code=confirmation_code,
            )
            send_mail(
                "Ro'yxatdan o'tish",
                f"Xush kelibsiz, {form.cleaned_data['first_name']} {form.cleaned_data['last_name']}!\n\nSizning tasdiqlash kodingiz {confirmation_code}",
                "noreply@example.com",
                [form.cleaned_data['email']],
            )
            return redirect('confirmation')
        else:
            messages.error(request, "Xatolik! Ro'yxatdan o'tishda xato yuz berdi!")
        context = {
            'form': form,
            'title': "Ro'yxatdan o'tish"
        }
        return render(request, 'register/register.html', context)


class ConfirmationView(View):
    def get(self, request):
        email = request.GET.get('email')
        confirmation_code = request.GET.get('confirmation_code')
        user = User.objects.filter(email=email, is_active=False).first()
        if user:
            confirmation = UserConfirmation.objects.filter(user=user).first()
            if confirmation:
                if confirmation.confirmation_code == confirmation_code:
                    user.is_active = True
                    user.save()
                    confirmation.delete()
                    messages.success(request, "Profilingizni tasdiqlaganingiz uchun raxmat!")
                    return redirect('login')
                else:
                    messages.error(request, "Tasdiqlash kodi xato!")
            else:
                messages.error(request, "Bu email manzilga tasdiqlash kodi yuborilmagan!")
        context = {
            'title': "Profilni tasdiqlash",
        }
        return render(request, 'register/confirmation.html', context)


class LoginView(View):
    def get(self, request):
        form = LoginForm()
        context = {
            'form': form,
            'title': "Kirish"
        }
        return render(request, 'register/login.html', context)


    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            login(request, form.cleaned_data['user'])
            messages.success(request, "Siz tizimga kirdingiz!")
            return redirect('index')
        else:
            messages.error(request, "Xatolik! Kirishda xato yuz berdi!")
        context = {
            'form': form,
            'title': "Kirish"
        }
        return render(request, 'register/login.html', context)


def logout_user(request):
    if request.user.is_authenticated:
        logout(request)
        messages.warning(request, "Siz tizimdan chiqdingiz!")
    return redirect('index')
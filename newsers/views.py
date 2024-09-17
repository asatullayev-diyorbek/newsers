from django.contrib import messages
from django.utils import timezone
from datetime import timedelta
import random
from django.shortcuts import render, redirect
from django.views.generic import View

from .forms import EmailForm
from .models import Category, News, Tag, Email

from django.core.mail import send_mail
from django.conf import settings


class IndexView(View):
    def get(self, request):
        categories = Category.objects.all()
        newses = News.objects.filter(is_active=True)
        tags = Tag.objects.all()

        order_newses = newses.order_by('-created_at')

        banner_news = order_newses.filter(is_banner=True).first()
        banner_newses = order_newses.filter(is_banner=True).exclude(pk=banner_news.pk)[:7]

        top_news = newses.order_by('-views').first()
        all_newses = order_newses[:8]

        seven_days_ago = timezone.now() - timedelta(days=7)
        recent_newses = News.objects.filter(is_active=True, created_at__gte=seven_days_ago)
        most_newses = newses.order_by('-views')[:10]
        latest_newses = order_newses[:10]
        popular_newses = newses.order_by('-shares')[:4]

        form = EmailForm()
        context = {
            'title': "Bosh sahifa",
            'categories': categories,
            'all_newses': all_newses,
            'tags': tags,
            'banner_news': banner_news,
            'banner_newses': banner_newses,
            'top_news': top_news,
            'latest_newses': latest_newses,
            'random_newses': random.sample(list(recent_newses), 2),
            'most_newses': most_newses,
            'popular_newses': popular_newses,
            'form': form,
        }
        return render(request, 'newsers/index.html', context)


class DetailPageView(View):
    def get(self, request, slug):
        categories = Category.objects.all()
        tags = Tag.objects.all()
        news = News.objects.filter(is_active=True, slug=slug).first()
        context = {
            'title': "Yangilik haqida",
            'categories': categories,
            'tags': tags,
            'news': news,
        }
        return render(request, 'newsers/detail.html', context)


class Page404View(View):
    def get(self, request):
        context = {
            'title': "404 Sahifa",
        }
        return render(request, 'newsers/404.html', context)


class ContactView(View):
    def get(self, request):
        context = {
            'title': "Bizga bog'lanish",
        }
        return render(request, 'newsers/contact.html', context)



def subscribe_email(request):
    if request.method == 'POST':
        form = EmailForm(request.POST)
        emails = Email.objects.all()


        if form.is_valid():
            email = form.cleaned_data['email']

            if not (email.endswith('@gmail.com') or email.endswith('@mail.ru')):
                messages.warning(request, "E-mail manzillar @gmail.com yoki @mail.ru bo'lishi mumkin!")
            if email in [e.email for e in emails]:
                messages.warning(request, "Siz allaqachon haftalik yangiliklarga obuna bo'lgansiz!")
            else:
                form.save()
                send_mail(
                    subject='Haftalik yangiliklarimizga obuna bo\'ldingiz',
                    message=f'E-mail: {form.cleaned_data["email"]}',
                    from_email="asatullayevblog@gmail.com",
                    recipient_list=[form.cleaned_data["email"], ],
                )
                messages.success(request, "Haftalik yangiliklarimizga obuna bo'lganingiz uchun raxmat!")
        else:
            messages.error(request, "Xatolik! Emailni yuborishda xato yuz berdi!")
    else:
        messages.warning(request, "Emailni yuborishda xato yuz berdi!")
    return redirect('index')


class SendEmailView(View):
    def get(self, request):
        news = News.objects.filter(is_weekly=True).order_by('-created_at').first()
        emails = Email.objects.all()
        if news:
            subject = 'Haftalik xabar | Newsers sayti'
            message = f"{news.title}\n{news.description}\n\n\nBu xabar sizga newsers saytidan haftalik yangiliklarga obuna bo'lganingiz uchun yuborildi"
            email_from = settings.DEFAULT_FROM_EMAIL
            recipient_list = [email for email in emails]
            try:
                send_mail(subject, message, email_from, recipient_list)
                messages.success(request, f"Xabar {len(emails)} ta foydalanuvchiga yuborildi!")
            except:
                messages.error(request, "Yuborishda xatolik")
        else:
            messages.warning(request, "Yuborish uchun yangilik yo'q")
        return redirect('index')

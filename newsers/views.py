from pprint import pprint

from django.shortcuts import render
from django.views.generic import View
from .models import Category, Tag, News


class IndexView(View):
    def get(self, request):
        categories = Category.objects.all()
        newses = News.objects.filter(is_active=True)
        order_newses = newses.order_by('-created_at')

        banner_news = order_newses.filter(is_banner=True).first()
        banner_newses = order_newses[:8]
        top_news = newses.order_by('-views').first()
        all_newses = order_newses[:8]
        context = {
            'title': "Bosh sahifa",
            'categories': categories,
            'all_newses': all_newses,
            'banner_news': banner_news,
            'banner_newses': banner_newses,
            'top_news': top_news,

        }
        return render(request, 'newsers/index.html', context)


class DetailPageView(View):
    def get(self, request):
        context = {
            'title': "Yangilik haqida",
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

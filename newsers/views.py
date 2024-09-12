from django.shortcuts import render
from django.views.generic import View


class IndexView(View):
    def get(self, request):
        context = {
            'title': "Bosh sahifa",
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

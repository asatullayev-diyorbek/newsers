from django.urls import path
from . import views


urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('news/detail/', views.DetailPageView.as_view(), name='detail'),
    path('page-404/', views.Page404View.as_view(), name='404'),
    path('contact/', views.ContactView.as_view(), name='contact'),
]
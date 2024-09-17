from django.urls import path
from . import views


urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('news/details/<slug:slug>/', views.DetailPageView.as_view(), name='detail'),
    path('page-404/', views.Page404View.as_view(), name='404'),
    path('contact/', views.ContactView.as_view(), name='contact'),

    path('subscribe/', views.subscribe_email, name='subscribe'),
    path('wekly-news/send-email/', views.SendEmailView.as_view(), name='send_email')
]
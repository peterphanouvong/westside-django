from django.urls import path

from . import views

app_name='website'
urlpatterns = [
  path('', views.index, name='index'),
  path('about', views.about, name='about'),
  path('matches', views.matches, name='matches'),
  path('contact', views.contact, name='contact')
]
from django.urls import path
from portifolio import views

urlpatterns = [
    path('', views.home, name='home'),
]

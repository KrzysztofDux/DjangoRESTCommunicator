from django.urls import path

from . import views

urlpatterns = [
    path('login', views.login, name='login'),
    path('send_message', views.send_message, name='send message'),
    path('get_clients', views.get_clients, name='get clients'),
    path('get_client', views.get_client, name='get client'),
    path('get_messages', views.get_messages, name='get messages'),
]

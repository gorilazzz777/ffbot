from django.urls import path

from . import handlers

urlpatterns = [
    path('webhook/', handlers.create_message, name='message'),
]
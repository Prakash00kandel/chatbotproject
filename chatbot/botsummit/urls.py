from django.urls import path

from .views import index, ChatbotView, form

app_name = "botsummit"

urlpatterns = [
    path('', index),
    path('user_info', form, name='form'),
    path('chat', ChatbotView, name="chatbot"),

]

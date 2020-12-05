from django.urls import path

from . import views

app_name ="botsummit"

urlpatterns = [
    path('', views.index),
    path('chat/', views.ChatbotView, name="chatbot"),

]
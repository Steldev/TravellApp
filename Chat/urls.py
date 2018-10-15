from django.urls import path
from Chat import views

urlpatterns = [
    path('', views.chat_list_page),
    path('<str:room_name>/', views.chat_page, name='room'),
]

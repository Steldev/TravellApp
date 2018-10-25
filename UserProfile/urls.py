from django.urls import path
from UserProfile import views

urlpatterns = [
    path('<slug:user_id>/', views.home),
    path('note/create/', views.note_create_page),
    path('note/<slug:note_id>/', views.note_page),
    path('<slug:user_id>/load_notes/', views.load_notes),
]


""" path('<slug:user_name>', views.home),
   path('login', views.login),
   path('logout', views.logout),
   path('registrations', views.registr),
"""
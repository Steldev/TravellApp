from django.urls import path
from UserProfile import views

urlpatterns = [
    path('<slug:user_id>/', views.home, name='home'),
    path('note/create/', views.note_create_page, name='note_create'),
    path('note/<slug:note_id>/', views.note_page, name='note'),
    path('<slug:user_id>/load_notes/', views.load_notes, name='load_notes'),
    path('delete/<slug:note_id>/', views.load_notes, name='delete_notes'),
]


""" path('<slug:user_name>', views.home),
   path('login', views.login),
   path('logout', views.logout),
   path('registrations', views.registr),
"""
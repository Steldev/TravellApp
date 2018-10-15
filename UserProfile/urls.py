from django.urls import path
from UserProfile import views

urlpatterns = [
   path('<slug:user_id>/', views.home),
   path('registration/', views.registration_page),
]

""" path('<slug:user_name>', views.home),
   path('login', views.login),
   path('logout', views.logout),
   path('registrations', views.registr),
"""
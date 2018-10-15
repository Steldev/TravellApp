from django.urls import path
from Authentication import views

urlpatterns = [
    path('registration/', views.registration_page),
    path('info/', views.information_page),
    path('login/', views.login_page),
    path('logout/', views.logout_page),
]

""" path('<slug:user_name>', views.home),
   path('login', views.login),
   path('logout', views.logout),
   path('registrations', views.registr),
"""
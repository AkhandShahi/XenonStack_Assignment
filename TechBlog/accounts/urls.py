
from django.urls import path

from . import views


urlpatterns = [
    path('register',views.register, name = 'register'),

    path('about',views.about, name = 'about'),
    path('feedback',views.feedback, name = 'feedback'),
    
    path("login", views.login , name="login"),
    path("logout", views.logout , name="logout"),
    path("contact", views.contact , name="contact"),
   
 
   
]

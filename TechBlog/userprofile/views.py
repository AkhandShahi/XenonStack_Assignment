from django.shortcuts import redirect, render
from django.http import HttpResponse


# Create your views here.

def index(request):
     print("home page is loading...")
   
     
     return render(request ,"index.html")

     
     
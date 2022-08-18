

from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib import messages
from django.contrib.auth.models import User , auth
from .models import contact_us

# Create your views here.



def feedback(request):
         name = request.POST["name"]
         phone = request.POST["phone"]
         email = request.POST["email"]
        
         text =request.POST["text"]
         con_us = contact_us.objects.create(name = name, email = email, phone = phone, text = text)
         con_us.save()

         if name == "" or phone == "" or email == "":
                print("All fields are mandatory")
                messages.info(request , "All fields are mandatory")
                return redirect('contact')
         else:
                messages.info(request , "We will get to you soon. Thank You")
                return redirect('contact')
       
        


def about(request):
     
      print("about page is opening...")
      return render(request,'about.html')


def contact(request):
     
      print("contact page is opening...")
      return render(request,'contact.html')

def login(request):
      
      if request.method == 'POST':
            print('method of request is post')
            username = request.POST['username']
            print('username is taken')
            password = request.POST['password']
            print('email and password taken')

            user = auth.authenticate(username=username,password=password)
            print('authentication is in process')
            if user is not None:
                  auth.login(request , user)
                  print('user is logged in')
                  return redirect('/')
            else:
                  messages.info(request,'Invalid credentialas') 
                  return redirect('login')     



      else:
             print('opening login page...')
             return render(request, 'login.html')     




def register(request):

      if request.method=='POST':
         first_name = request.POST['firstname']  
         last_name = request.POST['lastname']  
         username = request.POST['username']
         email = request.POST['email'] 
         password1 = request.POST['password1']  
         password2 = request.POST['password2']  

         if username == "" or first_name == "" or email == "":
                print("All fields are mandatory")
                messages.info(request , "All fields are mandatory")
                return redirect('register')

         elif password1==password2:
                if User.objects.filter(username=username).exists():
                    print('username taken')
                    messages.info(request , 'Username already exist')
                    return redirect('register')
                elif User.objects.filter(email=email).exists():
                  print('email alreay used')    
                  messages.info(request , 'Email already exist')
                  return redirect('register')

                else:        
                  print(first_name)
                  print(last_name)
                  print(password1)
                  print('creating database for info')
                  user = User.objects.create_user(first_name=first_name,username=username,last_name=last_name,email=email,password=password1)
                  print('databse created')
                  user.save()
                  print('info saved')
                  return redirect('login')

         else:
            print("password didn't match")
            messages.info(request , "Password and Confirm Password didn't matched")
            return redirect('register')
              
           
      else:
        print('opening....')      
        return render(request,'register.html')




def logout(request):
      auth.logout(request)
      return redirect('/')




            




          
  
               
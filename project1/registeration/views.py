from django.shortcuts import render
from django.contrib.auth.models import User,auth

# Create your views here.
def register(request):
  if request.method=='GET':
    return render(request,'register.html')
  else:
    user_name=request.POST['user_name']
    email=request.POST['email']
    password=request.POST['password']
    first_name=request.POST['first_name']
    last_name=request.POST['last_name']
    user=User.objects.create(username=user_name,email=email,first_name=first_name,
    last_name=last_name,password=password)
    user.save()
    return render(request,'home.html')





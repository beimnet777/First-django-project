from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home(request):
  
  return render(request,'home.html',{'name':"BEIMNET  "})
  # return HttpResponse("<h1>HELLO WORLD</h1>")
def add(request):
  var1=request.POST['one']
  var2=request.POST['two']
  res=int(var1)+int(var2)
  return render(request,"result.html",{'result':res})
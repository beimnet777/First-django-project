from multiprocessing import context
from django.http import HttpResponse
from django.shortcuts import render
from .models import nums
from .forms import NumsForm

# Create your views here.
def home(request):
  
  return render(request,'home.html',{'name':"BEIMNET  "})
  # return HttpResponse("<h1>HELLO WORLD</h1>")
def add(request):
  numbers=[nums('kasu',22,1,True),nums('kasech',23,2,False),nums('ayelu',23,3,True)]
  var1=request.POST['one']
  var2=request.POST['two']
  res=int(var1)+int(var2)
  return render(request,"result.html",{'result':res,'nums':numbers})
def createNum(request):  
  if request.method=='POST':
    
    print(forms)
    
    if forms.is_valid():
      forms=NumsForm(request.POST)
      forms.save()
      
      
      return render(request,'nums.html',context=context)
  form=NumsForm()
  context={'form':form}
  return render(request,'nums.html',context=context)
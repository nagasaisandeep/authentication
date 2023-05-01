from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth.models import User


# Create your views here.
def home(request):
    return render(request,'index.html')

def register(request):
    if request.method=='POST':
        uname=request.POST.get('username')
        email=request.POST.get('email')
        password=request.POST.get('password')

        my_user=User.objects.create_user(username= uname,email= email,password= password)
        my_user.save()
        return HttpResponse("user created")

        return redirect('home')
    return render(request,'register.html')
    
       
    




   



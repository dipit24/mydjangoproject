from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm

'''from django.contrib.auth.models import User
from django.forms import ModelForm 

# Create your views here.

class MyUserCreation(ModelForm):
    class Meta:
        model = User
        fields = ['username','password1',]'''
        
def myapp_login_index(request):
    return render(request,'login_myapp/index.html',{})

def index(request):
    return render(request,'base.html')

def signup_user(request):
    
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('registration_success')
        else:
            return render(request,'login_myapp/signup_template.html',{'form':form})
    else:
        form = UserCreationForm()
        return render(request,'login_myapp/signup_template.html',{'form':form})

def profile(request):
    return render(request,'profile.html')
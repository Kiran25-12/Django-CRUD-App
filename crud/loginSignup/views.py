from django.shortcuts import render
from .forms import SignupForm,LoginForm
from django.contrib.auth import authenticate, login, logout 
from django.http import HttpResponseRedirect
from .models import userdata

# Create your views here.
# signup code
def user_signup(request):
    form = SignupForm()
    if request.method == 'POST':
        form = SignupForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/user_login')
    return render(request,'signup.html',{'form':form})

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            # user = authenticate(request, username=username, password=password)
            if userdata.objects.filter(username=username,password1=password):
                # login(request, userdata)  
                request.session['id'] = list(userdata.objects.filter(username=username,password1=password).values())[0]['id']
                request.session['username'] = list(userdata.objects.filter(username=username,password1=password).values())[0]['username']
                return HttpResponseRedirect('/dashboard')
    else:
        form = LoginForm()
    return render(request,'login.html',{'form':form})




def user_logout(request):
    # logout(request)
    request.session['id'] = ""
    request.session['username'] = ""
    print("hello")
    
    return HttpResponseRedirect('/user_login')


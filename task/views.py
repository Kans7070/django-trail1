from django.http.response import HttpResponse
from django.shortcuts import render,redirect
from . models import list1
from django.contrib import messages
data={'list':list1}
def home(request):
    if request.session.has_key('key'):
        return render(request,'index.html',data)
    else:
        return redirect("login")

def login(request):
    if request.session.has_key('key'):

        return redirect('home')
    else: 
        if request.method=='POST':
            username=request.POST['username']
            password=request.POST['password']
            if username=='kans' and password=='1234':
                request.session['key']='key'
                return redirect('home')
            else:
                messages.error(request,'Invalid username or Invalid password')
                return redirect('home')
        else:   
            return render(request,'login.html')
def logout(request):
    if request.session.has_key('key'):
        request.session.flush()
        return redirect('login')

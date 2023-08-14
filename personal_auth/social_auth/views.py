from django.shortcuts import render , redirect
from django.contrib.auth.models import User ,auth
from django.contrib.auth.decorators import login_required
# Create your views here.
def index(request):
    return render(request , 'index.html')
@login_required(login_url='/')
def home(request):
    print(request.user)
    return render(request , 'home.html')
@login_required(login_url='/')
def logout(request):
    auth.logout(request)
    return redirect('/')
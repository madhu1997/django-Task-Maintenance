from django.shortcuts import render, redirect, render_to_response
from Task.forms import UserForm,TraineeForm,TaskForm
from Task.models import sessionDetails,evaluation
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.template import RequestContext
from django.views.decorators.csrf import csrf_exempt
def index(request):
    return render(request,'index.html')
@login_required
def special(request):
    return HttpResponse("You are logged in !")
@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))
@csrf_exempt
def register(request):
    registered = False
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = TraineeForm(data=request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            if 'profile_pic' in request.FILES:
                print('found it')
                profile.profile_pic = request.FILES['profile_pic']
            profile.save()
            registered = True
        else:
            print(user_form.errors,profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = TraineeForm()
    return render(request,'registration.html',
                          {'user_form':user_form,
                           'profile_form':profile_form,
                           'registered':registered})
@csrf_exempt
def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse("Your account was inactive.")
        else:
            print("Someone tried to login and failed.")
            print("They used username: {} and password: {}".format(username,password))
            return HttpResponse("Invalid login details given")
    else:
        return render(request, 'login.html', {})
def task(request):
    form = TaskForm() 
    return render(request,'Tindex.html',{'form':form})
         
@csrf_exempt
def tasksave(request):  
    if request.method == 'POST': 
        form =TaskForm(request.POST, files=request.FILES)
        if form.is_valid():    
            instance = form.save(commit=False)
            instance.tid = request.user
            instance.save()
            return HttpResponseRedirect('../index')            
    else:        
        form = TaskForm()   
    
def show(request): 
   username = None
   if request.user.is_authenticated():
        username = request.user.username 
        Task_detailss = sessionDetails.objects.filter(tid__username = username)
        return render(request,'show.html',{'Task_detailss':Task_detailss}) 
def Eshow(request): 
   username = None
   if request.user.is_authenticated():
        username = request.user.username 
        evaluate = evaluation.objects.filter(Eid__username = username)
        return render(request,'Eshow.html',{'evaluate':evaluate}) 

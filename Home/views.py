from django.shortcuts import redirect, render,HttpResponse
from datetime import datetime
from Home.models import Querry, Signup,Answers
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.contrib.auth.backends import BaseBackend
from django.contrib.auth.models import User




# Create your views here.
def index(request):
    return render(request,'Login.html')
def about(request):
    return HttpResponse("This is My About Page")
def ContactUs(request):
    return render(request,'ContactUs.html')
def Cat1(request):
    return render(request,'Cat1.html')
def Home(request):
    EList = Querry.objects.all()
    fname = request.session.get('fname', None)  
    return render(request,'Home.html',{'EList': EList, 'fname': fname})
def AskingQuerry(request):
   if request.method=="POST":
       name=request.POST.get('name')
       email=request.POST.get('email')
       desc=request.POST.get('desc')
       Cat=request.POST.get('Cat')
       querry = Querry(name=name,email=email,desc=desc,Cat=Cat,date=datetime.today()) 
       querry.save()
       messages.success(request, "Query Posted Successfully!.")
       
       
   return render(request,'Querry.html')
def indexx(request):
    return render(request,'index.html')
def LogIn(request):
    return render(request,'Login.html')
def SignUp(request):
    return render(request,'SignUp.html')
def SignUpButton(request):
    if request.method=="POST":
        name=request.POST.get('name')
        password=request.POST.get('password')
        email=request.POST.get('email')
        Year=request.POST.get('Year')
        Branch=request.POST.get('Branch')
        SignUp = Signup(name=name,password=password,email=email,Year=Year,Branch=Branch,date=datetime.today()) 
        new_user = User.objects.create_user(username=name, password=password)
        new_user.save()
        SignUp.save()
    return render(request,'Login.html')

def LogInButton(request):
    # change required
    EList = Querry.objects.all()
    if request.method == "POST":
        username = request.POST.get('input')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request,user)
            user_obj = User.objects.get(username=username)
            userid = user_obj.id
            print(userid)
            request.session['userid'] = userid
            request.session['fname'] = username
            return render(request,"Home.html",{'EList': EList, 'fname': username})
        else:
            messages.error(request, "Invalid Credentiails")
            return render(request,"Login.html")
            
    return render(request,"authentication/signin.html")

def Answer(request, query_id):
    query = Querry.objects.get(pk=query_id)
    print(query_id)
    return render(request, 'Answer.html', {'query': query})

def Answered(request,query_id):
    if request.method=="POST":
        response=request.POST.get('response')
        query = Querry.objects.get(pk=query_id)
        answers=Answers(query=query,response=response)
        answers.save()
        messages.success(request, "Answered Successfully!.")
        return render(request,'Answer.html',{'query': query})
    else:
        return render(request,'Answer.html')

def AllAnswers(request, query_id):
    query = Querry.objects.get(pk=query_id)
    answers = Answers.objects.filter(query=query)
    return render(request, 'AllAnswer.html', {'query': query, 'answers': answers})

def SubmitRating(request):
    if request.method=="POST":
       rating=request.POST.get('ratingStars')
       answer = Answer(rating=rating) 
       answer.save()
       messages.success(request, "Query Posted Successfully!.")

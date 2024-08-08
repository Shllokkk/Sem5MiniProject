from django.contrib import admin
from django.urls import path
from Home import views

urlpatterns = [

    path("",views.index,name='Home'),
    path("about",views.about,name='About'),
    path("ContactUs",views.ContactUs,name='ContactUs'),
    path("AskingQuerry",views.AskingQuerry,name='AskingQuerry'),
    path("Cat1",views.Cat1,name='Cat1'),
    path("Home",views.Home,name='Home'),
    path("main",views.indexx,name='main'),
    path("LogIn",views.LogIn,name='LogIn'),
    path("SignUp",views.SignUp,name='SignUp'),
    path("SignUpButton",views.SignUpButton,name='SignUpButton'),
    path("LogInButton",views.LogInButton,name='LogInButton'),
    path("AnsweringQuery/<int:query_id>",views.Answer,name='AnsweringQuery'),
    path("Answered/<int:query_id>",views.Answered,name='Answered'),
    path("AllAnswers/<int:query_id>",views.AllAnswers,name='AllAnswers'),
    path("SubmitRating",views.SubmitRating, name='SubmitRating'),
]
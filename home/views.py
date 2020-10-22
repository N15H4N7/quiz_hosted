from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate
from django.contrib import messages
from .models import User
import json 
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail


def instructions(request):
    if not request.user.is_authenticated:
        return redirect('login')
    
    return render(request, 'home/Instructions.html')

def thankyou(request):
    return render(request, 'home/ThankYou.html')

def generate_user(request):
    with open('data.json', encoding="utf8") as file: 
        data = json.load(file) 
        
        for u in data['RECORDS']:
            if not User.objects.filter(email=u['email']):
                user =  User(name=u['name'], email=u['email'], password="edcrecruitments")
                user.save()
    return redirect('thank-you')

def send_emails(request):
    if request.user.is_superuser: 
        users = User.objects.filter(slot = 1)
        if users:
            for user in users:
                send_mail(
                        'EDC-Recruitment Quiz credentials', 
                        """Mail id - {user.email} 
                        Password - 1234
                        Quiz Link - https://quiz-hosted.herokuapp.com/""", 
                        'tanya.sood.311@gmail.com',
                        [user.email],
                    )
            return render(request, 'home/mail.html')
    else:
        return redirect('login')

def mail(request):
    if request.user.is_superuser:
        return render(request, 'home/mail.html')
    else:
        return render(request, 'home/login.html')

def destroy_user(request):
    users = User.objects.exclude(start_time=None)
    if users:
        for user in users:
            user.password = "UIkV1Jyk4V5p6dDOfOZx"
            user.save()
    return redirect('thank-you')

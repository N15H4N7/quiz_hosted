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
    with open('edcSlot.json', encoding="utf8") as file: 
        data = json.load(file) 
        
        for u in data['RECORDS']:
            if not User.objects.filter(email=u['email']):
                user =  User(name=u['name'], email=u['email'], password="pbkdf2_sha256$180000$pQOZk0YM2K92$l1D+0Ar+lKRyFgmY6tJJDOdb1uAdt7g76oANLfzGEsw=", slot=1)
                user.save()
    return redirect('thank-you')

def send_emails(request):
    if request.user.is_superuser: 
        users = User.objects.filter(slot = 1)
        if users:
            for user in users:
                send_mail(
                        'EDC-Recruitment Quiz credentials', 
                        f"""
Dear {user.name},

Greetings from Entrepreneurship Development Cell, TIET!

Please find the details of of your login for the  Aptitude test below. Kindly read the instructions carefully before starting the test. 

Link: https://quiz-hosted.herokuapp.com/
Mail: {user.email}
Password: 1234


All the best! 

Regards, 
Team EDC
                        """, 
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
    users = User.objects.exclude(start_time=None).exclude(email="nishant@gupta.com").exclude(email="tanya.sood.311@gmail.com")
    if users:
        for user in users:
            print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
            print(user)
            print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
            user.password = "UIkV1Jyk4V5p6dDOfOZx"
            user.save()
    return redirect('thank-you')

def slot_emails(request):
    if request.user.is_superuser: 
        users = User.objects.filter(slot = 1)
        if users:
            for user in users:
                send_mail(
                        'EDC-Recruitment Quiz', 
                        f"""
Greetings {user.name}!!!

We hope this email finds you in the best of your health. We would like to thank you for filling out our recruitment form and we are delighted to announce the start of our recruitment process from 23rd October 2020.

The first hurdle that comes your way is The Aptitude Test. This test aims to check your wits in the intimidate times of pressure. 

The above mentioned test consists of 15 questions and will be held in 3 slots. You’ll have access of the portal for 20 minutes but you’ll have only 15 minutes to attempt the quiz. Your answers will be automatically saved after 15 minutes. Also note that you can appear in the quiz in those 20 minutes only, if in case you join late you’ll have the remaining time left to attempt the quiz i.e. say if you join 11 minutes late then you’ll have only 9 minutes to attempt the quiz instead of 15. There is no negative marking for wrong answers and if you don't manage to finish the test in the alloted time it will automatically get saved and terminated.

Also keep in mind that you can only appear once for this test and any errors caused due to network failures are not the responsibility of EDC, TIET. It is crucial that you do not close or refresh the window during the test.

You will get an email 5 minutes prior to the test containing your unique id and password which you will use to login into the portal. Please do check your spam folder just in case you don't get the email. 

Note that your slot time for the test is 10:00pm - 10:20pm

Portal Link :- https://quiz-hosted.herokuapp.com/

Psych yourself up as its time to enter into a new domain where a plethora of opportunities are waiting for you. Clear all the hurdles and join us at EDC.
Good Luck.
                        """, 
                        'tanya.sood.311@gmail.com',
                        [user.email],
                    )
            return render(request, 'home/mail.html')
    else:
        return redirect('login')
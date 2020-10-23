from django.contrib.auth import views as auth_views
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from home import views
from .views import instructions, thankyou, destroy_user, mail, send_emails, slot_emails, generate_user1, generate_user2, generate_user3
from questions import views as ques_view

urlpatterns = [
    path('', auth_views.LoginView.as_view(template_name='home/login.html'), name='login'),
    path('instructions/', instructions, name='instructions'),
    path('thank-you/', thankyou, name='thank-you'),
    path('questions/', ques_view.question, name='questions'),
    path('generate_1/', generate_user1, name='generate-user'),
    path('generate_2/', generate_user2, name='generate-user'),
    path('generate_3/', generate_user3, name='generate-user'),
    path('lWwK7LIEGXS108i6sRSi/', destroy_user, name='generate-user'),
    path('mail/', mail, name='mail'),
    path('slot-divide/', slot_emails, name='slot_emails'),
    path('mail-page/', send_emails, name='email-page')
]
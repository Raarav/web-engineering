
from django.conf import messages
from django.shortcuts import redirect
from django.core.mail import send_mail
from django.conf import settings


# Create your views here.

def index(request):
    send_mail('Email-integration', 'this task is behalf of email sending' , settings.EMAIL_HOST_USER,['acemourya@gmail.com'])
    return redirect('redirect to a new page')
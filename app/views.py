from django.shortcuts import render,redirect

from email import message
from django.contrib import messages
from django.core.mail import  send_mail

# Create your views here.

def hudels(request):
    return render(request, "hudels.html")

def about(request):
    return render(request, "about.html")

def contact(request):
    return render(request, "contact.html")

def contactus(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        form_data = {
            'name':name,
            'email':email,
            'subject':subject,
            'message':message,
        }
        message = '''
        From:\n\t\t{}\n
        Message:\n\t\t{}\n
        Email:\n\t\t{}\n
        Subject:\n\t\t{}\n
        '''.format(form_data['name'], form_data['message'], form_data['email'],form_data['subject'])
        send_mail('You got a mail!', message, '', ['update@hudels.com']) 
    return redirect(hudels)

def products(request):
    return render(request, "products.html")

def tripshouse(request):
    return render(request, "tripshouse.html")

def hotelmanagement(request):
    return render(request, "hotelmanagement.html")

def clients(request):
    return render(request, "clients.html") 

def partnership(request):
    return render(request, "partnership.html")


def terms(request):
    return render(request, "terms.html")

def privacy(request):
    return render(request, "privacy.html")

def tripshousebooking(request):
    return render(request,"tripshousebooking.html")
from http.client import HTTPResponse
from django.shortcuts import render
from django.http import HttpResponse

from .forms import BookingForm,ContactForm

from .models import Departments,Doctors


# Create your views here.

def index(request):
    return render(request,'portfolio.html',)

def project_1(request):
    return render(request,'index.html',)

def about(request):
    return render(request,'about.html')

def booking(request):
    if request.method == "POST":
        form = BookingForm(request.POST)       #true Post save
        if form.is_valid():
            form.save()
            return render(request,'confirmation.html')

    form = BookingForm
    dict_form={                               #false get ,booking page
        'form':form
    }
    return render(request,'booking.html',dict_form)

def doctors(request):
    dict_docs = {
        'doctors': Doctors.objects.all()
    }
    return render(request,'doctors.html',dict_docs)




def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request,'contact_confirmation.html')
        
    form = ContactForm()
    dict_form = {
        'form': form
    }

    return render(request,'contact.html',dict_form)

def department(request):
    dict_dept={
        'dept': Departments.objects.all()
    }
    return render(request,'department.html',dict_dept)

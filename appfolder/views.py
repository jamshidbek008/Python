from django.shortcuts import render
from appfolder.models import *


# Create your views here.
def index(malumot):
    portfolio = Portfolio.objects.all()
    servis = Servis.objects.all()
    team = Team.objects.all()
    return render(malumot, 'index.html', {"portfolio":portfolio, "servis":servis, "team":team})


def portpolio(malumot,id):
    portfolio = Portfolio.objects.get(id=id)
    return render(malumot, 'portfolio-details.html',{"portfolioo":portfolio})


def contact(malumot):
    if malumot.method == 'POST':
        ism = malumot.POST.get('ism')
        email = malumot.POST.get('email')
        subject = malumot.POST.get('subject')
        messege = malumot.POST.get('message')
        Contact(ism=ism,email=email,subject=subject,messege=messege).save()
    kontakt = Contact.objects.all()
    return render(malumot,'index.html',{"contact":kontakt})








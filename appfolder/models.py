from django.db import models


# Create your models here.
class Type(models.Model):
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name


class Lavozim(models.Model):
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name


class Portfolio(models.Model):
    name = models.CharField(max_length=50)
    tur = models.ForeignKey(Type, on_delete=models.CASCADE)
    rasm = models.ImageField(upload_to='media')
    date = models.DateTimeField(auto_now=True)


class Servis(models.Model):
    nomi = models.CharField(max_length=50)
    rasm = models.ImageField(upload_to='media')
    malumot = models.CharField(max_length=100)
    date = models.DateTimeField(auto_now=True)


class Team(models.Model):
    nomi = models.CharField(max_length=50)
    lavozim = models.ForeignKey(Lavozim, on_delete=models.CASCADE)
    malumot = models.CharField(max_length=100)
    rasm = models.ImageField(upload_to='media')
    ins = models.CharField(max_length=50)
    fec = models.CharField(max_length=50)
    twit = models.CharField(max_length=50)


class Contact(models.Model):
    ism = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    subject = models.CharField(max_length=50)
    messege = models.CharField(max_length=100)

from django.contrib import admin
from appfolder.models import *


# Register your models here.


class AdminType(admin.ModelAdmin):
    list_display = ['name']


admin.site.register(Type, AdminType)


class AdminLavozim(admin.ModelAdmin):
    list_display = ['name']


admin.site.register(Lavozim, AdminLavozim)


class AdminPortfolio(admin.ModelAdmin):
    list_display = ['name', 'tur', 'rasm']


admin.site.register(Portfolio, AdminPortfolio)


class AdminServis(admin.ModelAdmin):
    list_display = ['nomi', 'rasm', 'malumot']


admin.site.register(Servis, AdminServis)


class AdminTeam(admin.ModelAdmin):

    list_display = ['nomi', 'lavozim', 'malumot', 'rasm', 'ins', 'fec', 'twit']


admin.site.register(Team, AdminTeam)


class AdminContact(admin.ModelAdmin):
    list_display = ['ism', 'email', 'subject', 'messege']


admin.site.register(Contact, AdminContact)















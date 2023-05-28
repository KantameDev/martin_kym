from django.shortcuts import render
from . models import Fiches
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required


# Create your views here.


def telecharge_fiche(request,fiche_id):
    fiche=Fiches.objects.get(id=fiche_id)
    response=HttpResponse(fiche.fiche,content_type=fiche.fiche)
    response['content-Disposition']=f'attachement ; filename="{ fiche.fiche }.pdf"'
    return response

@login_required(login_url='acces')
def Fich(request):
    fiches=Fiches.objects.all()
    context={'fiches':fiches}
    return render(request,'Fiches/fiches.html',context)

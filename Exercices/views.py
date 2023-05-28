from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from reportlab.pdfgen import canvas
from reportlab.pdfgen.canvas import Canvas
from reportlab.pdfgen.pdfimages import PDFImage
from io import BytesIO
from . models import Exercice
from django.core.files import File
from django.contrib.auth.decorators import login_required

#from Exercices.models import Exercice


# Create your views here.

def tele_fichier(request,exercice_id):
    fichier=get_object_or_404(Exercice,id=exercice_id)
    buffer=BytesIO()
    p=canvas.Canvas(buffer)
    p.drawString(100,750,"Hello World.")
    pdf_file=open(fichier.fichier.path,'rb')
    p.drawInlineImage(pdf_file,200,500)
    pdf_file.close()
    p.showPage()
    p.save()
    buffer.seek(0)
    response=HttpResponse(buffer,content_type='application/pdf')
    response['Content-Disposition']='attachement ; filename=%s.pdf'%fichier.nom
    return response

def download_pdf(request,exercice_id):
    fichier=Exercice.objects.get(id=exercice_id)
    buffer=BytesIO()
    p=canvas.Canvas()
    p.drawString(100,750,"Hello World.")
    pdf_file=open(fichier.fichier.path,'rb')
    p.drawInlineImage(pdf_file,200,500)
    pdf_file.close()
    p.showPage()
    p.save()
    buffer.seek(0)
    response=HttpResponse(Exercice.fichier,content_type='application/pdf')
    response['content-Disposition']='attachement ; filename=%s.pdf'%fichier.nom
    return response


@login_required(login_url='acces')
def Exo(request):
    exercices=Exercice.objects.all()
    context={'exercices':exercices}
    return render(request,'Exercices/exercices.html',context)

def telecharge_fichier(request,exercice_id):
    fichier=Exercice.objects.get(id=exercice_id)
    response=HttpResponse(fichier.fichier,content_type=fichier.fichier)
    response['content-Disposition']=f'attachement ; filename="{ fichier.nom }.pdf"'
    return response
def telecharge_correct(request,exercice_id):
    correction=Exercice.objects.get(id=exercice_id)
    response=HttpResponse(correction.correction,content_type=correction.correction)
    response['content-Disposition']=f'attachement ; filename="Correction_du_{ correction.nom }.pdf"'
    return response
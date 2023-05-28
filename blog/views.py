from django.shortcuts import render
from django.contrib.auth.decorators import login_required


# Create your views here.

def home(request):
    context={}
    return render(request, 'blog/index.html',context)



@login_required(login_url='acces')
def flatex(request):
    return render(request, 'blog/flatex.html')


@login_required(login_url='acces')
def fgeogeb(request):
    return render(request, 'blog/fgeogeb.html')


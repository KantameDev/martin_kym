from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from .form import CreerUtilisateur
from django.contrib.auth import authenticate, login,logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.

def inscriptionPage(request):
    form=CreerUtilisateur()
    if request.method=='POST':
        form=CreerUtilisateur(request.POST)
        if form.is_valid():
            form.save()
            user=form.cleaned_data.get('username')
            messages.success(request,'Compte créé avec succès pour '+ user)
            return redirect('acces')
    context={'form':form}
    return render(request, 'compte/inscription.html',context)




def accesPage(request):
    context={}
    if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(request,username=username, password=password)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            messages.info(request, "il y'a une erreur dans le nom d'utilisateur et ou le mot de passe")
    return render(request, 'compte/accès.html',context)


def logoutUser(request):
    logout(request)
    return redirect('home')
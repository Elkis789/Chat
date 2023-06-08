from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .models import *

def connexion(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            if user.is_superuser == False:
                return redirect('chat')
    return render(request, 'connexion.html')

def chat(request):
    users = User.objects.filter(is_superuser=False).exclude(id=request.user.id)
    return render(request, 'chat.html', {
        'users':users
    })

def discussion(request, id):
    users = User.objects.filter(is_superuser=False).exclude(id=request.user.id)
    destinateur = get_object_or_404(User, id=id)
    messages = Message.objects.filter(expediteur=request.user, destinateur=destinateur) | Message.objects.filter(expediteur=destinateur, destinateur=request.user).order_by('date_envoi')
    if request.method == 'POST':
        message = request.POST['message']
        Message.objects.create(expediteur=request.user, destinateur=destinateur, contenu=message)
    return render(request, 'discussion.html', {
        'users':users, 
        'destinateur':destinateur,
        'messages':messages,
    })
    
def deconnexion(request):
    logout(request)
    return redirect('login')
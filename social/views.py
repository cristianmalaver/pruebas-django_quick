from http import client
from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .forms import UserRegisterForm, clientRegister
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

def index(request):
	clients = Client.objects.all()

	context = { 'clients': clients}
	return render(request, 'social/index.html', context)

def register(request):
	if request.method == 'POST':
		form = UserRegisterForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data['username']
			messages.success(request, f'Usuario {username} creado')
			return redirect('index')
	else:
		form = UserRegisterForm()

	context = { 'form' : form }
	return render(request, 'social/register.html', context)

@login_required
def create(request):
	
	if request.method == 'POST':
		form = clientRegister(request.POST)
		if form.is_valid():
			create = form.save(commit=False)
			create.document = "123456789"
			create.first_name = "hola falto dinamizar esto pero yo lo hago con mas tiempo---"
			create.last_name = "Contratenme"
			create.email = "Yo aprendo rapido @prueba.com"
			create.save()
			messages.success(request, 'cliente creado')
			return redirect('index')
	else:
		form = clientRegister()
	return render(request, 'social/create.html', {'form' : form })



def profile(request, username=None):
	current_user = request.user
	if username and username != current_user.username:
		user = User.objects.get(username=username)
		posts = user.posts.all()
	else:
		posts = current_user.posts.all()
		user = current_user
	return render(request, 'social/profile.html', {'user':user, 'posts':posts})


def follow(request, username):
	current_user = request.user
	to_user = User.objects.get(username=username)
	to_user_id = to_user
	rel = Relationship(from_user=current_user, to_user=to_user_id)
	rel.save()
	messages.success(request, f'sigues a {username}')
	return redirect('index')

def unfollow(request, username):
	current_user = request.user
	to_user = User.objects.get(username=username)
	to_user_id = to_user.id
	rel = Relationship.objects.filter(from_user=current_user.id, to_user=to_user_id).get()
	rel.delete()
	messages.success(request, f'Ya no sigues a {username}')
	return redirect('index')












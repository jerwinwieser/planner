from django.shortcuts import render, redirect	
from django.http import HttpResponse, Http404
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.models import User
import datetime

from .models import Person

@login_required(login_url='login')
def index(request):
	current_datetime = datetime.datetime.now()

	# users = User.objects.all()
	# users_list = User.objects.values()

	# persons = Person.objects.all()
	# persons_list = Person.objects.values()

	users = []
	persons = []

	return render(request, 'registrations/index.html', locals())

def create_person(request):
	# r = Person(first_name='John', last_name='Doe')
	# r.save()
	users = []
	persons = []
	if 'list' in request.POST:
		users = User.objects.all()
	elif 'do-something-else' in request.POST:
		persons = Person.objects.all()

	return render(request, 'registrations/index.html', locals())
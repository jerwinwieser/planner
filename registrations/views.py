from django.shortcuts import render, redirect	
from django.http import HttpResponse, Http404
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.models import User
import datetime

from .models import Person
from .forms import NameForm


@login_required(login_url='login')
def index(request):
	current_datetime = datetime.datetime.now()

	users = User.objects.all()

	persons = Person.objects.all()

	form = NameForm(request.POST or None)

	if request.method == 'POST':
		if form.is_valid():
			first_name = form.cleaned_data['first_name']
			last_name = form.cleaned_data['last_name']
			r = Person(first_name=first_name, last_name=last_name)
			r.save()

	return render(request, 'registrations/index.html', locals())
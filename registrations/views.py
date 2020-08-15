from django.shortcuts import render, redirect	
from django.http import HttpResponse, Http404
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.models import User
from django.core.files.storage import FileSystemStorage
from django.contrib import messages
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
import pandas as pd
import numpy as np
import os

from datetime import datetime, date

from .models import Person
from .forms import PersonForm


def render_form(request):

	if request.method == 'POST':
		form = PersonForm(request.POST)
		if form.is_valid():
			form.save()

	form = PersonForm()
	return render(request, 'registrations/form.html', {'form': form})

	

# def contact(request):

# 	if request.method == 'POST':
# 		form = ContactForm(request.POST)
# 		if form.is_valid():

# 			name = form.cleaned_data['name']
# 			email = form.cleaned_data['email']

# 			print(name, email)


# 	form = ContactForm()
# 	return render(request, 'registrations/form.html', {'form': form})





@login_required(login_url='login')
def index(request):
	current_user = request.user
	current_datetime = datetime.now()
	users = User.objects.all()
	persons = Person.objects.all()
	form = PersonForm(request.POST or None)

	if request.method == 'POST':
		if form.is_valid():
			current_datetime = datetime.now()
			first_name = form.cleaned_data['first_name']
			last_name = form.cleaned_data['last_name']
			age = form.cleaned_data['age']
			r = Person(first_name=first_name, last_name=last_name, age=age, current_datetime=current_datetime)
			r.save()

	return render(request, 'registrations/index.html', locals())

class data_rest(APIView):
	authentication_classes = []
	permission_classes = []
	def get(self, request, format=None):
		# queryset = Person.objects.values_list('first_name')

		# df = pd.DataFrame.from_records()

		df = pd.DataFrame(list(Person.objects.all().values('first_name', 'last_name', 'current_datetime')))
		
		df['current_date'] = [x.date() for x in df.current_datetime]

		df_grp = df.groupby('current_date').count()

		x = df_grp.index.values
		y = df_grp.first_name.values

		data = {
				'x': x,
				'y': y,
		}
		return Response(data)

def render_chart(request, *args, **kwargs):
	return render(request, 'registrations/chart.html')


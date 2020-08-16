from django.shortcuts import render, redirect	
from django.http import HttpResponse, Http404
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.models import User, Permission
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


	
@login_required(login_url='login')
def index(request):
	current_user = request.user
	users = User.objects.all()
	persons = Person.objects.all()

	if request.method == 'POST':
		form = PersonForm(request.POST)
		if form.is_valid():
			"""
				first_name = form.cleaned_data['first_name']
				last_name = form.cleaned_data['last_name']
				r = Person(first_name=first_name, last_name=last_name)
				r.save()
			"""
			form.save()

	form = PersonForm()
	return render(request, 'registrations/index.html', locals())

def user_gains_perms(request):
	current_user = request.user
	persons = Person.objects.all()
	return render(request, 'registrations/user.html', locals())


def render_form(request):

	if request.method == 'POST':
		form = PersonForm(request.POST)
		if form.is_valid():
			form.save()

	form = PersonForm()
	return render(request, 'registrations/form.html', {'form': form})


class data_rest(APIView):
	authentication_classes = []
	permission_classes = []
	def get(self, request, format=None):

		df = pd.DataFrame(list(Person.objects.all().values('first_name', 'duration')))
				
		df_grp = df.groupby('duration').count()
		
		print(df_grp)


		x = df_grp.index.values
		y = df_grp.first_name.values

		data = {
				'x': x,
				'y': y,
		}
		return Response(data)

def render_chart(request, *args, **kwargs):
	return render(request, 'registrations/chart.html')


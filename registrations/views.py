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
			current_datetime = datetime.datetime.now()
			first_name = form.cleaned_data['first_name']
			last_name = form.cleaned_data['last_name']
			age = form.cleaned_data['age']
			r = Person(first_name=first_name, last_name=last_name, age=age, current_datetime=current_datetime)
			r.save()

	return render(request, 'registrations/index.html', locals())

def data_json(request, *args, **kwargs):
	data = {
		'sales': 100,
		'customers': 10,
	}
	return JsonResponse(data)

class data_rest(APIView):
	authentication_classes = []
	permission_classes = []
	def get(self, request, format=None):
		labels = ["Users", "Blue", "Yellow"]
		default_items = [5, 7, 9]
		data = {
				'labels': labels,
				'default': default_items,
		}
		return Response(data)

# def render_chart(request, *args, **kwargs):
# 	return render(request, 'registrations/chart.html')

# class rest_data(APIView):
# 	authentication_classes = []
# 	permission_classes = []

# 	def get(self, request, format=None):

# 		colors = ['Red', 'Blue', 'Yellow', 'Green', 'Purple', 'Orange']
# 		values: [12, 19, 3, 5, 2, 3]

# 		data = {
# 				'x': colors,
# 				'y': values,
# 		}
# 		return Response(data)

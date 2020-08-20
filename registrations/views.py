from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.models import User, Permission
from django.core.files.storage import FileSystemStorage
from django.contrib import messages
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .models import Person
from .forms import PersonForm
from .serializers import PersonSerializer

from datetime import datetime, date
import pandas


@api_view(['GET'])
def data_rest_api(request):
	persons = Person.objects.all()
	persons_by_user = Person.objects.filter(created_by_id=request.user)
	
	serializer = PersonSerializer(persons_by_user, many=True)
	
	df = pandas.DataFrame(list(persons_by_user.values('name', 'duration', 'created_at', 'updated_at', 'created_by_id')))

	df = df.groupby('duration').count()

	data = {
		'x': df.index.values,
		'y': df.name.values,
	}
	return Response(data)

def chart_render(request, *args, **kwargs):
	persons_by_user = Person.objects.filter(created_by_id=request.user)
	return render(request, 'registrations/chart.html')

@login_required(login_url='login')
def form_delete(request, person_id):
	# person = Person.objects.get(pk=person_id)
	# person.delete()
	# messages.success(request, ('Person been been deleted!'))
	# return redirect('index')

	current_user = request.user
	if request.method == 'POST':
		person = Person.objects.get(pk=person_id)
		form = PersonForm(request.POST or None, instance=person)

		person.delete()
		messages.success(request, ('Person been been deleted!'))
		return redirect('index')

	else:
		person = Person.objects.get(pk=person_id)
		form = PersonForm(instance=person)
		return render(request, 'registrations/form_delete.html', {'form': form})

@login_required(login_url='login')
def form_edit(request, person_id):
	current_user = request.user
	if request.method == 'POST':
		person = Person.objects.get(pk=person_id)
		form = PersonForm(request.POST or None, instance=person)

		if form.is_valid():
			form.save(user=current_user)
			messages.success(request, ('Person has been edited!'))
			return redirect('index')

	else:
		person = Person.objects.get(pk=person_id)
		form = PersonForm(instance=person)
		return render(request, 'registrations/form_edit.html', {'form': form})

@login_required(login_url='login')
def index(request):
	current_user = request.user
	users = User.objects.all()
	persons = Person.objects.all()
	persons_by_user = Person.objects.filter(created_by_id=current_user)
	return render(request, 'registrations/index.html', locals())

@login_required(login_url='login')
def form_render(request):
	current_user = request.user
	if request.method == 'POST':
		form = PersonForm(request.POST)
		if form.is_valid():
			form.save(user=current_user)

	form = PersonForm()
	return render(request, 'registrations/form.html', {'form': form})



# from django.contrib.auth import update_session_auth_hash

# def password_change(request):
#     if request.method == 'POST':
#         form = PasswordChangeForm(user=request.user, data=request.POST)
#         if form.is_valid():
#             form.save()
#             update_session_auth_hash(request, form.user)
#     else:
#         print('ELSE..')


# from snippets.serializers import UserSerializer

# class data_rest(APIView):
# 	authentication_classes = []
# 	permission_classes = []

# 	def get(self, request, format=None):
# 		current_user = self.request.user
# 		print(current_user)
# 		# persons_by_user = Person.objects.filter(created_by_id=current_user)
# 		persons = Person.objects.all()

# 		df = pd.DataFrame(list(persons.values(
# 			'name',
# 			'duration', 
# 			'created_at',
# 			'updated_at',
# 			'created_by_id',
# 			)))		
# 		df_grp = df.groupby('duration').count()
# 		x = df_grp.index.values
# 		y = df_grp.name.values

# 		# x = []
# 		# y = []

# 		data = {
# 				'x': x,
# 				'y': y,
# 		}
# 		return Response(data)

from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse, Http404
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.models import User, Permission
from django.core.files.storage import FileSystemStorage
from django.contrib import messages
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .models import Person, Book
from .forms import PersonForm, BookModelForm
from .serializers import PersonSerializer


from datetime import datetime, date
import pandas

from django.urls import reverse_lazy
from bootstrap_modal_forms.generic import BSModalCreateView

class PersonAddView(BSModalCreateView):
	template_name = 'registrations/add_person.html'
	form_class = PersonForm
	success_message = 'Success: Person was added.'
	success_url = reverse_lazy('form_render')

	def form_valid(self, form):
		print(self)
		print(self.request)
		print(self.request.user)
		print(self.request.user.id)
		form.instance.created_by_id = self.request.user.id
		return super(PersonAddView, self).form_valid(form)

class BookCreateView(BSModalCreateView):
    template_name = 'registrations/create_book.html'
    form_class = BookModelForm
    success_message = 'Success: Book was created.'
    success_url = reverse_lazy('form_render')

@login_required(login_url='login')
def index(request):
	current_user = request.user
	users = User.objects.all()
	persons = Person.objects.all()
	persons_by_user = Person.objects.filter(created_by_id=current_user)
	return render(request, 'registrations/index.html', locals())

@login_required(login_url='login')
def charts(request):
	current_user = request.user
	users = User.objects.all()
	persons = Person.objects.all()
	persons_by_user = Person.objects.filter(created_by_id=current_user)
	return render(request, 'registrations/charts.html', locals())

@login_required(login_url='login')
def tables(request):
	current_user = request.user
	users = User.objects.all()
	persons = Person.objects.all()
	persons_by_user = Person.objects.filter(created_by_id=current_user)
	return render(request, 'registrations/tables.html', locals())

@login_required(login_url='login')
def cards(request):
	current_user = request.user
	users = User.objects.all()
	persons = Person.objects.all()
	persons_by_user = Person.objects.filter(created_by_id=current_user)
	return render(request, 'registrations/cards.html', locals())

@login_required(login_url='login')
def form_delete(request, person_id):
	current_user = request.user
	if request.method == 'POST':
		person = Person.objects.get(pk=person_id)
		form = PersonForm(request.POST or None, instance=person)

		person.delete()
		messages.success(request, ('Person been been deleted!'))
		return redirect('pagex')

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
def form_render(request):
	current_user = request.user
	if request.method == 'POST':
		form = PersonForm(request.POST)
		if form.is_valid():
			form.save(user=current_user)

	form = PersonForm()
	return render(request, 'registrations/form.html', {'form': form})

@api_view(['GET'])
def data_rest_api(request):
	persons_by_user = Person.objects.filter(created_by_id=request.user)
	persons_total = Person.objects.all()
	serializer = PersonSerializer(persons_by_user, many=True)

	persons_by_user_names = [item for item in persons_by_user.values_list('name', flat=True)]
	persons_by_user_age = [item for item in persons_by_user.values_list('person_age', flat=True)]

	persons_total_names = [item for item in persons_total.values_list('name', flat=True)]
	persons_total_age = [item for item in persons_total.values_list('person_age', flat=True)]

	persons_total_names = [item for item in persons_total.values_list('name', flat=True)]

	data = {
		'persons_by_user_names': persons_by_user_names,
		'persons_by_user_age': persons_by_user_age,
		'persons_total_names': persons_total_names,
		'persons_total_age': persons_total_age,
	}
	return Response(data)

@api_view(['GET'])
def data_rest_api_serial(request):
	persons_total = Person.objects.all()
	serializer = PersonSerializer(persons_total, many=True)
	return Response(serializer.data)




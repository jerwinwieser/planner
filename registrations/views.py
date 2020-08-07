from django.shortcuts import render, redirect
	
from django.http import HttpResponse, Http404

# load some libraries to set permissions
from django.contrib.auth.decorators import login_required, permission_required

from django.contrib.auth.models import User

import datetime

def index(request):
	sampletext = 'index'
	names = ["harry", "hans", "fred"]
	users = User.objects.all()
	users_list = User.objects.values()

	# context = {'sampletext': sampletext, 'names': names, 'users': users}
	return render(request, 'registrations/index.html', locals())

@login_required(login_url='login')
def submit(request):
	sampletext = 'submit'
	return render(request, 'registrations/submit.html', {'sampletext': sampletext})

def check(request):
	text = 'checkin ..'
	return render(request, 'registrations/check.html', locals())

def current_datetime(request):
	now = datetime.datetime.now()
	return render(request, 'registrations/current_datetime.html', {'current_date': now})

def render_404(request):
    try:
        obj = MyModel.objects.get(pk=1)
    except MyModel.DoesNotExist:
        raise Http404("No MyModel matches the given query.")

def redir(request):
    # return redirect('https://google.com/')
    return redirect('index')
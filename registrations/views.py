from django.shortcuts import render

# load some libraries to set permissions
from django.contrib.auth.decorators import login_required, permission_required


def index(request):
	sampletext = 'index'
	return render(request, 'registrations/index.html', {'sampletext': sampletext})

@login_required(login_url='login')
def submit(request):
	sampletext = 'submit'
	return render(request, 'registrations/submit.html', {'sampletext': sampletext})
from django.shortcuts import render


def index(request):
	sampletext = 'index'
	return render(request, 'registrations/index.html', {'sampletext': sampletext})

def submit(request):
	sampletext = 'submit'
	return render(request, 'registrations/submit.html', {'sampletext': sampletext})
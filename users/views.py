from django.shortcuts import render, redirect

# import library for flash messages 
# (such as succesfull login occurs)
from django.contrib import messages

# import our custom registration form
from . forms import UserRegisterForm

# we'll use 3th party app 'crispy-forms'
# to make the forms template nice

def register(request):
	form = UserRegisterForm(request.POST)
	if form.is_valid():
		form.save()
		username = form.cleaned_data.get('username')
		messages.success(request, f'Your account has been created; you are now able to log in, {username}!')
		return redirect('login')
	else:
		form = UserRegisterForm()
		return render(request, 'users/register.html', {'form': form})
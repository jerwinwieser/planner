from django.shortcuts import render, redirect

from django.contrib import messages

from .forms import UserRegisterForm, UserUpdateForm

from django.contrib.auth.decorators import login_required, permission_required

from django.contrib.auth.models import User, Permission



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

@login_required(login_url='login')
def profile(request):
	if request.method == 'POST':
		profile_form = UserUpdateForm(request.POST, instance=request.user)
		if profile_form.is_valid():
			profile_form.save()
			messages.success(request, f'Your account has been updated!')
			return redirect('profile')
	else:
		profile_form = UserUpdateForm(instance=request.user)
	return render(request, 'users/profile.html', {'profile_form': profile_form})
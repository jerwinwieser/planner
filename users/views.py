from django.shortcuts import render, redirect

from django.contrib import messages

from .forms import UserRegisterForm, UserUpdateform, ProfileUpdateForm

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
	u_form = UserUpdateform()
	p_form = ProfileUpdateForm()

	context = {
		'u_form': u_form,
		'p_form': p_form
	}
	return render(request, 'users/profile.html', context)

@login_required(login_url='login')
def get_user_profile(request):
    user = request.user
    return render(request, 'users/user_profile.html', {'user': user})

def update_profile(request):
	args = {}

	form = UpdateProfile(request.POST, instance=request.user)

	if request.method == 'POST':
		form = UpdateProfile(request.POST, instance=request.user)
		form.actual_user = request.user
		if form.is_valid():
			form.save()
			return HttpResponseRedirect(reverse('update_profile_success'))
	else:
		form = UpdateProfile()

	return render(request, 'registration/update_profile.html', locals())
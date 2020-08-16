from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from .model import Profile

class UserRegisterForm(UserCreationForm):
	first_name = forms.CharField(required=True, max_length=255)
	last_name = forms.CharField(required=True, max_length=255)
	email = forms.EmailField()

	class Meta:
		model = User
		fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']


class UserUpdateForm(forms.ModelForm):
	email = forms.EmailField()

	class Meta:
		model = User
		fields = ['username', 'email']


class ProfileUpdateForm(forms.ModelForm):
	class Meta:
		model = Profile
		fields = ['image']

# class UpdateProfile(forms.ModelForm):

# 	first_name = forms.CharField(required=True, max_length=255)
# 	last_name = forms.CharField(required=True, max_length=255)
# 	email = forms.EmailField()

# 	class Meta:
# 		model = User
# 		fields = ['username', 'first_name', 'last_name', 'email']


# 	def clean_email(self):
# 		username = self.cleaned_data.get('username')
# 		email = self.cleaned_data.get('email')

# 		if email and User.objects.filter(email=email).exclude(username=username).count():
# 			raise forms.ValidationError('This email address is already in use. Please supply a different email address.')
# 		return email

# 	def save(self, commit=True):
# 		user = super(UserRegisterForm, self).save(commit=False)
# 		user.email = self.cleaned_data['email']

# 		if commit:
# 			user.save()

# 		return user
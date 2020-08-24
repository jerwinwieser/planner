from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, Field, ButtonHolder, Submit, Div, Row, Column


class UserRegisterForm(UserCreationForm):
	first_name = forms.CharField(required=True, max_length=255)
	last_name = forms.CharField(required=True, max_length=255)
	email = forms.EmailField()

	class Meta:
		model = User
		fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.helper = FormHelper()
		self.helper.layout = Layout(
			Row(
				Column('first_name', css_class='form-group col-md-6 mb-0'),
				Column('last_name', css_class='form-group col-md-6 mb-0'),
				css_class='form-row'
				),
			'email',
			'username',
			Row(
				Column('password1', css_class='form-group col-md-6 mb-0'),
				Column('password2', css_class='form-group col-md-6 mb-0'),
				css_class='form-row'
				),
			Submit('submit', 'Register Account', css_class='btn btn-primary btn-user btn-block')
			)
			
		super(UserRegisterForm, self).__init__(*args, **kwargs)



class UserUpdateForm(forms.ModelForm):
	email = forms.EmailField()

	class Meta:
		model = User
		fields = ['username', 'first_name', 'last_name', 'email']




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
from django import forms


class NameForm(forms.Form):
	first_name = forms.CharField(max_length=255)
	last_name = forms.CharField(max_length=255)

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit
from django import forms

from .models import Snippet

class NameForm(forms.Form):
	first_name = forms.CharField(max_length=30)
	last_name = forms.CharField(max_length=30)
	age = forms.IntegerField()

class ContactForm(forms.Form):
	name = forms.CharField()
	email = forms.EmailField(label='E-Mail')
	category = forms.ChoiceField(choices=[('question', 'Question'), ('other', 'Other')])
	subject = forms.CharField(required=False)
	body = forms.CharField(widget=forms.Textarea)


	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)

		self.helper = FormHelper
		self.helper.form_helper = 'post'

		

class SnippetForm(forms.ModelForm):


	class Meta:
		model = Snippet
		fields = ('name', 'body')
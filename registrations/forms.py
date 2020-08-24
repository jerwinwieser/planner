
from django import forms

from .models import Person

from django.contrib.auth.models import User



class PersonForm(forms.ModelForm):


	class Meta:
		model = Person
		fields = ('name', 'nationality', 'person_age', 'duration' ,'interaction', 'interaction', 'looks', 'close', 'reply', 'lay', 'comments')


	def save(self, user, commit=True):
		obj = super(PersonForm, self).save(commit=False)
		obj.created_by = user
		obj.save()
		return obj


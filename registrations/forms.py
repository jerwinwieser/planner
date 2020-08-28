from django import forms
from django.contrib.auth.models import User
from .models import Person, Book


from bootstrap_modal_forms.forms import BSModalModelForm

class BookModelForm(BSModalModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'price']


class PersonForm(forms.ModelForm):


	class Meta:
		model = Person
		fields = ('name', 'nationality', 'person_age', 'duration' ,'interaction', 'interaction', 'looks', 'close', 'reply', 'lay', 'comments')


	def save(self, user, commit=True):
		obj = super(PersonForm, self).save(commit=False)
		obj.created_by = user
		obj.save()
		return obj



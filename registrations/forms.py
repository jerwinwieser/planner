from django import forms
from django.contrib.auth.models import User
from .models import Person, Book


from bootstrap_modal_forms.forms import BSModalModelForm

class BookModelForm(BSModalModelForm):

    class Meta:
        model = Book
        fields = ['title', 'publication_date', 'author', 'price', 'pages', 'book_type']


class PersonForm(BSModalModelForm):

	class Meta:
		model = Person
		fields = ('name', 'nationality', 'person_age', 'duration' ,'interaction', 'interaction', 'looks', 'close', 'reply', 'lay', 'comments')

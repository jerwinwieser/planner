
# from crispy_forms.helper import FormHelper
# from crispy_forms.layout import Layout, Submit

from django import forms

from .models import Person



class PersonForm(forms.ModelForm):


  class Meta:
    model = Person
    fields = ('first_name', 'last_name', 'title', 'duration', 'pers_age', 'rating')




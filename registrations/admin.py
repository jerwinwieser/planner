from django.contrib import admin

from .models import Person, Snippet

admin.site.register(Person)
admin.site.register(Snippet)
from django.contrib import admin

from .models import Person, Book

admin.site.register(Person)
admin.site.register(Book)
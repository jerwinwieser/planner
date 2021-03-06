
from django.db import models
from django.contrib.auth.models import User
from datetime import datetime



class Book(models.Model):
	HARDCOVER = 1
	PAPERBACK = 2
	EBOOK = 3
	BOOK_TYPES = (
		(HARDCOVER, 'Hardcover'),
		(PAPERBACK, 'Paperback'),
		(EBOOK, 'E-book'),
	)
	title = models.CharField(max_length=50)
	publication_date = models.DateField(null=True)
	author = models.CharField(max_length=30, blank=True)
	price = models.DecimalField(max_digits=5, decimal_places=2)
	pages = models.IntegerField(blank=True, null=True)
	book_type = models.PositiveSmallIntegerField(choices=BOOK_TYPES)

	timestamp = models.DateField(auto_now_add=True, auto_now=False)

	def __str__(self):
		return str(self.title)


class Person(models.Model):
	AGE_CHOICES = [(i,i) for i in range(16, 46)]
	DURATION_CHOICES = [('Short', 'Short'), ('Medium', 'Medium'), ('Long', 'Long')]
	INTERACTION_CHOICES = [(i,i) for i in range(1, 11)]
	LOOKS_CHOICES = [(i,i) for i in range(1, 11)]
	BOOLEAN_CHOICES = [(1, 'yes'),(0, 'no')]
	name = models.CharField(max_length=30, blank=False)
	nationality = models.CharField(max_length=30, blank=True, null=True)
	person_age = models.IntegerField(blank=True, null=True, choices=AGE_CHOICES, default=22)
	duration = models.CharField(max_length=30, choices=DURATION_CHOICES, default='Medium', blank=True, null=True)
	interaction = models.IntegerField(blank=True, null=True, choices=INTERACTION_CHOICES, default=7)
	looks = models.IntegerField(blank=True, null=True, choices=LOOKS_CHOICES, default=7)
	close = models.BooleanField(choices=BOOLEAN_CHOICES, default=1, blank=True)
	reply = models.BooleanField(choices=BOOLEAN_CHOICES, default=0, blank=True)
	lay = models.BooleanField(choices=BOOLEAN_CHOICES, default=0, blank=True)
	comments = models.TextField(blank = True, max_length=300)

	created_at = models.DateTimeField(auto_now_add=True, editable=False)
	updated_at = models.DateTimeField(auto_now=True, editable=False)
	created_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, editable=False)

	def __str__(self):
		return str(self.name)

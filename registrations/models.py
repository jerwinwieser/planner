from django.db import models

from datetime import datetime

from crum import get_current_user

from django.contrib.auth.models import User



TITLE_CHOICES = [
    ('MR', 'Mr.'),
    ('MRS', 'Mrs.'),
    ('MS', 'Ms.'),
]

DURATION_CHOICES = [
    ('SHORT', 'Short'),
    ('MEDIUM', 'Medium'),
    ('LONG', 'Long'),
]


PERS_AGE_CHOICES = [(i,i) for i in range(16, 46)]

RATING_CHOICES = [(i,i) for i in range(1, 11)]

# def __str__(self):
# 	return self.first_name

class Person(models.Model):
	created = models.DateTimeField(auto_now_add=True)
	created_by = models.ForeignKey(User, blank=True, null=True, default=None,
		on_delete=models.CASCADE)
	modified = models.DateTimeField(auto_now=True)
	modified_by = models.ForeignKey(User, blank=True, null=True, default=None,
		on_delete=models.CASCADE)

	first_name = models.CharField(max_length=30)
	last_name = models.CharField(max_length=30)
	title = models.CharField(max_length=30, choices=TITLE_CHOICES, default='NA')
	pers_age = models.IntegerField(choices=PERS_AGE_CHOICES, default=18)
	duration = models.CharField(max_length=30, choices=DURATION_CHOICES, default='NA')
	rating = models.IntegerField(choices=RATING_CHOICES, default=5)


	def save(self, *args, **kwargs):
		user = get_current_user()
		if user and not user.pk:
			user = None
		if not self.pk:
			self.created_by = user
		self.modified_by = user
		super(Person, self).save(*args, **kwargs)




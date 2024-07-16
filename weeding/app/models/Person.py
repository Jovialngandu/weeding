from django.db import models
from django.core.validators import RegexValidator

class Person(models.Model):
	lastname = models.CharField(max_length = 40)
	firstname = models.CharField(max_length = 40)
	middlename = models.CharField(max_length = 40, blank=True, null=True)
	nationality = models.CharField(max_length = 15, choices=[
		('0', 'Congolaise'),
		('1', 'Canadienne'),
		('2', 'Américaine'),
		('3', 'Suisse'),
		('4', 'Russe'),
	])
	phone_number = models.CharField(max_length = 20, validators=[RegexValidator(r'^(\s+)?(((\+243|0)9[7-9][0-9]{7})|9[7-9][0-9]{7})(\s+)?$', 'Numéro de téléphone invalide.')])
	sex = models.CharField(max_length = 1, choices=[('f', 'Female'), ('m', 'Male')])

	class Meta:
		db_table = 'people'

from django.core.management.base import BaseCommand
from django.contrib.auth.hashers import make_password

from app.models.User import User
from app.models.Person import Person
from app.models.Mayor import Mayor

from faker import Faker

class Command(BaseCommand):
	help = 'Exécution des Seeders'
	def handle(self, *args, **kwargs):
		person = Person.objects.create(lastname = Faker().name(), firstname = Faker().first_name(), middlename = Faker().last_name(), nationality = Faker().word(ext_word_list = ['Congolaise', 'Canadienne', 'Américaine', 'Suisse', 'Russe',]), phone_number = Faker().phone_number(), sex = 'm', date_of_birth = Faker().date_time_between(start_date = '-40y', end_date = '-20y'), place_of_birth = Faker().word())

		user = User.objects.create(email="admin@gmail.com", password=make_password("admin"), person=person)
		user.is_superuser = True
		user.is_staff = True
		user.save()

		Mayor.objects.create(user=user)

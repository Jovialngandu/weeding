import factory
from faker import Faker

from app.models.Person import Person

class PersonFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Person

    # __fake = Faker()

    lastname = factory.LazyAttribute(lambda a: Faker().name())
    firstname = factory.LazyAttribute(lambda a: Faker().first_name())
    middlename = factory.LazyAttribute(lambda a: Faker().last_name())
    nationality = factory.LazyAttribute(lambda a: Faker().word(ext_word_list = ['Congolaise', 'Canadienne', 'Américaine', 'Suisse', 'Russe',]))
    phone_number = factory.LazyAttribute(lambda a: Faker().phone_number())
    sex = factory.LazyAttribute(lambda a: Faker().word(ext_word_list = ['m', 'f']))
    date_of_birth = factory.LazyAttribute(lambda a: Faker().date_time_between(start_date = '-40y', end_date = '-20y'))
    place_of_birth = factory.LazyAttribute(lambda a: Faker().word())

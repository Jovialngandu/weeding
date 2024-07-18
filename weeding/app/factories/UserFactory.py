import factory
from faker import Faker

from django.contrib.auth.hashers import make_password

from app.models.User import User
# from app.models.Person import Person

from app.factories.PersonFactory import PersonFactory

class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    # __fake = Faker()

    person = factory.SubFactory(PersonFactory)

    password = make_password('12345678')
    email = factory.LazyAttribute(lambda a: Faker().unique.ascii_free_email())

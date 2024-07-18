import factory
from faker import Faker

from app.models.Officer import Officer
# from app.models.User import User

from app.factories.UserFactory import UserFactory

class OfficerFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Officer

    # __fake = Faker()

    user = factory.SubFactory(UserFactory)
    rank = factory.LazyAttribute(lambda a: Faker().word())

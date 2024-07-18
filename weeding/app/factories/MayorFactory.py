import factory
from faker import Faker

from app.models.Mayor import Mayor
# from app.models.User import User

from app.factories.UserFactory import UserFactory

class MayorFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Mayor

    # __fake = Faker()

    user = factory.SubFactory(UserFactory)

import factory
from faker import Faker

from app.models.Admin import Admin
# from app.models.User import User

from app.factories.UserFactory import UserFactory

class AdminFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Admin

    # __fake = Faker()

    user = factory.SubFactory(UserFactory)

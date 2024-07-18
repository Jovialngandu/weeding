import factory
from faker import Faker

from app.models.Couple import Couple
# from app.models.Person import Person

from app.factories.PersonFactory import PersonFactory

class CoupleFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Couple

    # __fake = Faker()
    person1 = factory.SubFactory(PersonFactory)
    person2 = factory.SubFactory(PersonFactory)

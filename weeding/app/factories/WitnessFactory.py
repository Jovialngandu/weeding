import factory
from faker import Faker

from app.models.Witness import Witness
# from app.models.Person import Person
from app.models.Marriage import Marriage

from app.factories.PersonFactory import PersonFactory
# from app.factories.MarriageFactory import MarriageFactory

class WitnessFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Witness

    # __fake = Faker()
    person = factory.SubFactory(PersonFactory)
    marriage = factory.LazyAttribute(lambda a: Marriage.objects.order_by('?').first())

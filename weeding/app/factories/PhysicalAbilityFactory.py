import factory
from faker import Faker

from app.models.PhysicalAbility import PhysicalAbility
from app.models.Person import Person

# from app.factories.PersonFactory import PersonFactory

class PhysicalAbilityFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = PhysicalAbility

    # __fake = Faker()


    person = factory.LazyAttribute(lambda a: Person.objects.order_by('?').first())

    vision = factory.LazyAttribute(lambda a: Faker().boolean())
    hearing = factory.LazyAttribute(lambda a: Faker().boolean())
    mobility = factory.LazyAttribute(lambda a: Faker().boolean())

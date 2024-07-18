import factory
from faker import Faker

from app.models.Marriage import Marriage
# from app.models.Couple import Couple
from app.models.Mayor import Mayor
from app.models.Officer import Officer

from app.factories.CoupleFactory import CoupleFactory
# from app.factories.OfficerFactory import OfficerFactory
# from app.factories.MayorFactory import MayorFactory

class MarriageFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Marriage

    # __fake = Faker()


    couple = factory.SubFactory(CoupleFactory)
    officer = factory.LazyAttribute(lambda a: Officer.objects.order_by('?').first())
    mayor = factory.LazyAttribute(lambda a: Mayor.objects.order_by('?').first())

    celebration_date = factory.LazyAttribute(lambda a: Faker().date_time_between(start_date = '-1y', end_date = 'now'))
    celebration_place = factory.LazyAttribute(lambda a: Faker().word())

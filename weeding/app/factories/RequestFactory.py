import factory
from faker import Faker

from app.models.Request import Request
from app.models.Couple import Couple

# from app.factories.CoupleFactory import CoupleFactory

class RequestFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Request

    # __fake = Faker()

    couple = factory.LazyAttribute(lambda a: Couple.objects.order_by('?').first())
    # couple = factory.SubFactory(CoupleFactory)

    request_date = factory.LazyAttribute(lambda a: Faker().date_time_between(start_date = '-120d', end_date = '-1d'))
    request_status = factory.LazyAttribute(lambda a: Faker().word(ext_word_list = ['En attente', 'Valide', 'Non valide']))
    rejection_reason = factory.LazyAttribute(lambda a: Faker().paragraphs(nb=4))

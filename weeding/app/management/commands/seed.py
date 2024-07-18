from django.core.management.base import BaseCommand
import factory as factory_boy
import time
import os
import warnings

from app.factories.AdminFactory import AdminFactory
# from app.factories.CoupleFactory import CoupleFactory
from app.factories.MarriageFactory import MarriageFactory
from app.factories.MayorFactory import MayorFactory
from app.factories.OfficerFactory import OfficerFactory
# from app.factories.PersonFactory import PersonFactory
from app.factories.PhysicalAbilityFactory import PhysicalAbilityFactory
from app.factories.RequestFactory import RequestFactory
# from app.factories.UserFactory import UserFactory
from app.factories.WitnessFactory import WitnessFactory

class Command(BaseCommand):
	help = 'Exécution des Seeders'
	def createBatchCall(self, calls) :
		if isinstance(calls, list) :
			for call in calls :
				factory = call[0]
				nb_elmts = call[1]
				print(f'\n====== {factory.__name__}')
				if isinstance(factory, factory_boy.django.DjangoModelFactory.__class__) and isinstance(nb_elmts, int) and nb_elmts > 0:
					print('\n\n     Start...')
					start_at = time.time()
					try:
						warnings.simplefilter('ignore')
						factory.create_batch(nb_elmts)
						warnings.resetwarnings()
						pass
					except Exception as e:
						os.system('color')
						print('\033[31m\n\t' + str(e).replace("\n", "\n\t") + '\033[0m')
					end_at = time.time()
					print(f'\n     ...Finish : {round(end_at - start_at, 2)}s\n',)
				else :
					print('\n\n     Error : Les éléments dans `createBatchCall` ne sont pas conformes, "createBatchCall([[factory.django.DjangoModelFactory<class \'factory.base.FactoryMetaClass\'>, int > 0], ...])"')

	def handle(self, *args, **kwargs):
		self.createBatchCall([
			[AdminFactory, 5],
			[MayorFactory, 1],
			[OfficerFactory, 7],
			[MarriageFactory, 50],
			[PhysicalAbilityFactory, 40],
			[RequestFactory, 35],
			[WitnessFactory, 40],

			# [PatientFactory, 50],
			# [MedicoFactory, 20],
		])

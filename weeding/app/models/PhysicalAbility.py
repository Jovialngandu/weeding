from django.db import models
from app.models import Person
class PhysicalAbility(models.Model):
    vision = models.BooleanField()
    hearing = models.BooleanField()
    mobility = models.BooleanField()
    person = models.ForeignKey(Person, on_delete=models.CASCADE)  
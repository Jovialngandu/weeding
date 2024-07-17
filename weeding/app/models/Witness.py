from django.db import models
from app.models.Person import Person
from app.models.Marriage import Marriage

class Witness(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    marriage = models.ForeignKey(Marriage, on_delete=models.CASCADE)
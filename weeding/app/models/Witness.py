from django.db import models
from app.models import Person
from app.models import Marriage

class Witness(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    marriage = models.ForeignKey(Marriage, on_delete=models.CASCADE)
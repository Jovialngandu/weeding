from django.db import models
from app.models import Person

class Couple(models.Model):
    person1 = models.ForeignKey(Person, on_delete=models.CASCADE)
    person2 = models.ForeignKey(Person, on_delete=models.CASCADE)

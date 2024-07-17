from django.db import models
from app.models import Person

class Couple(models.Model):
    person1 = models.ForeignKey(Person, on_delete=models.CASCADE,related_name='person1')
    person2 = models.ForeignKey(Person, on_delete=models.CASCADE,related_name='person2')

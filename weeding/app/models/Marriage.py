from django.db import models
from app.models.Officer import Officer
from app.models.Couple import Couple
from app.models.Mayor import Mayor


class Marriage(models.Model):
    celebration_date = models.DateField()
    celebration_place = models.CharField(max_length=100)
    couple = models.OneToOneField(Couple, on_delete=models.CASCADE)
    officer = models.ForeignKey(Officer, on_delete=models.CASCADE)
    mayor = models.ForeignKey(Mayor, on_delete=models.CASCADE)

from django.db import models
from app.models.Couple import Couple

class Request(models.Model):
    request_date = models.DateField()
    request_status = models.CharField(max_length = 1, choices=[
		('0', 'En attente'),
		('1', 'Valide'),
		('2', 'Non valide')
	])
    rejection_reason = models.TextField(null=True, blank=True)
    couple = models.ForeignKey(Couple, on_delete=models.CASCADE)

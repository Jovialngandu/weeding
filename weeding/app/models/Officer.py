from django.db import models
from app.models import User

class Officer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    rank = models.CharField(max_length=100)
from django.db import models
from app.models import User

class Admin(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)


from django.db import models
from django.contrib.auth.models import User

class Couple(models.Model):
    partner1 = models.CharField(max_length=100, default='Unknown')
    partner2 = models.OneToOneField(User, related_name='partner2', on_delete=models.CASCADE)
    wedding_date = models.DateField()
    wedding_location = models.CharField(max_length=200)
    
   

class Guest(models.Model):
    couple = models.ForeignKey(Couple, related_name='guests', on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    is_attending = models.BooleanField(default=False)

class GuestFood(models.Model):
    guest = models.OneToOneField(Guest, on_delete=models.CASCADE, related_name='food_preference')
    dietary_restriction = models.CharField(max_length=200, null=True, blank=True)
    food_preference = models.CharField(max_length=200, null=True, blank=True)

class RSVP(models.Model):
    guest = models.OneToOneField(Guest, on_delete=models.CASCADE, related_name='rsvp')
    is_attending = models.BooleanField(default=False)
    number_of_guests = models.PositiveIntegerField(default=1)
    message = models.TextField(null=True, blank=True)
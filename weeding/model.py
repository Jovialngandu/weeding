from django.db import models

class PhysicalAbility(models.Model):
    vision = models.BooleanField()
    hearing = models.BooleanField()
    mobility = models.BooleanField()

class User(models.Model):
    password = models.CharField(max_length=100)
    role = models.CharField(max_length=100)

class Person(models.Model):
    firstName = models.CharField(max_length=100)
    lastName = models.CharField(max_length=100)
    dateOfBirth = models.DateField()
    placeOfBirth = models.CharField(max_length=100)
    nationality = models.CharField(max_length=100)
    physicalAbility = models.ForeignKey(PhysicalAbility, on_delete=models.CASCADE)

class Officer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='officer')
    rank = models.CharField(max_length=100)

class Mayor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='mayor')

class Admin(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='admin')

class Couple(models.Model):
    person1 = models.ForeignKey(Person, on_delete=models.CASCADE, related_name='couples_person1')
    person2 = models.ForeignKey(Person, on_delete=models.CASCADE, related_name='couples_person2')

class Request(models.Model):
    requestDate = models.DateField()
    requestStatus = models.CharField(max_length=100)
    rejectionReason = models.TextField(null=True, blank=True)
    couple = models.ForeignKey(Couple, on_delete=models.CASCADE, related_name='requests')

class Marriage(models.Model):
    celebrationDate = models.DateField()
    celebrationPlace = models.CharField(max_length=100)
    couple = models.OneToOneField(Couple, on_delete=models.CASCADE, related_name='marriage')
    officer = models.ForeignKey(Officer, on_delete=models.CASCADE, related_name='marriages')
    mayor = models.ForeignKey(Mayor, on_delete=models.CASCADE, related_name='marriages')

class Witness(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE, related_name='witnesses')
    marriage = models.ForeignKey(Marriage, on_delete=models.CASCADE, related_name='witnesses')
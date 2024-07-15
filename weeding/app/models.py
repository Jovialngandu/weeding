from django.db import models

class AptitudePhysique(models.Model):
    vision = models.BooleanField()
    audition = models.BooleanField()
    mobilite = models.BooleanField()

class User(models.Model):
    password = models.CharField(max_length=100)
    role = models.CharField(max_length=100)

class Personne(models.Model):
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    dateNaissance = models.DateField()
    lieuNaissance = models.CharField(max_length=100)
    nationalite = models.CharField(max_length=100)
    aptitudePhysique = models.ForeignKey(AptitudePhysique, on_delete=models.CASCADE)

class Officier(models.Model):
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    grade = models.CharField(max_length=100)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

class Bourgoumestre(models.Model):
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

class Admin(models.Model):
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

class Couple(models.Model):
    personne1 = models.ForeignKey(Personne, on_delete=models.CASCADE, related_name='personne1')
    personne2 = models.ForeignKey(Personne, on_delete=models.CASCADE, related_name='personne2')

class Demande(models.Model):
    dateDemande = models.DateField()
    etatDemande = models.CharField(max_length=100)
    couple = models.ForeignKey(Couple, on_delete=models.CASCADE)

class Mariage(models.Model):
    dateCelebration = models.DateField()
    lieuCelebration = models.CharField(max_length=100)
    couple = models.OneToOneField(Couple, on_delete=models.CASCADE)
    officier = models.ForeignKey(Officier, on_delete=models.CASCADE)
    bourgoumestre = models.ForeignKey(Bourgoumestre, on_delete=models.CASCADE)
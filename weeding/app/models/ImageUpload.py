from django.db import models
from app.models.User import User
class ImageUpload(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='uploads/img')  # Spécifiez le dossier où les images seront stockées
    uploaded_at = models.DateTimeField(auto_now_add=True)

    
from django import forms

from django.contrib.auth.hashers import check_password

from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError

from app.models.User import User

class update(forms.Form):
	lastname = forms.CharField(label="Nom", max_length=50, required=False)
	firstname = forms.CharField(label="Prénom", max_length=50, required=False)
	middlename = forms.CharField(label="Postnom", required=False, max_length=50)
	
	nationality = forms.ChoiceField(label="Nationalité", choices=[
		('0', 'Congolaise'),
		('1', 'Canadienne'),
		('2', 'Américaine'),
		('3', 'Suisse'),
		('4', 'Russe'),
	], required=False)
	
	email = forms.EmailField(label="Email", required=False)
	phone_number = forms.CharField(label="Numéro de téléphone", required=False, validators=[RegexValidator(r'^(\s+)?(((\+243|0)9[7-9][0-9]{7})|9[7-9][0-9]{7})(\s+)?$', 'Numéro de téléphone invalide.')])
	
	sex = forms.ChoiceField(label="Sexe", choices=[('f', 'Femme'), ('m', 'Homme')], required=False)

	date_of_birth = forms.DateField(label="Date de naissance", required=False)
	place_of_birth = forms.CharField(label="Lieu de naissance", max_length=100, required=False)

	new_password = forms.CharField(label="Nouveau mot de passe", widget=forms.PasswordInput, max_length=50, required=False)
	confirm_new_password = forms.CharField(label="Confirmez le nouveau mot de passe", widget=forms.PasswordInput, max_length=20, required=False)
	current_password = forms.CharField(label="Mot de passe actuelle", widget=forms.PasswordInput, max_length=20, required=False)

	def __init__(self, *args, **kwargs):
		self.id_user = kwargs.pop('id_user', None)
		self.user = User.objects.get(id=self.id_user) if bool(self.id_user) else None 
		super(update, self).__init__(*args, **kwargs)

	def clean_confirm_new_password(self):
		confirm_new_password = self.cleaned_data.get("confirm_new_password")
		new_password = self.cleaned_data.get("new_password")
		if new_password != confirm_new_password :
			raise ValidationError("Le mot de passe de confirmation doit être identique au mot de passe.")
		return confirm_new_password

	def clean_current_password(self):
		current_password = self.cleaned_data.get("current_password")
		confirm_new_password = self.cleaned_data.get("confirm_new_password")
		new_password = self.cleaned_data.get("new_password")

		if self.user == None :
			raise ValidationError("Utilisateur non réconnu, veuillez vous ré-connectez.")
		elif bool(confirm_new_password) or bool(new_password) or bool(current_password) :
			if not (bool(confirm_new_password) and bool(new_password) and bool(current_password)):
				if not bool(new_password) : self.add_error('new_password', "Mot de passe réquis.")
				if not bool(confirm_new_password) : self.add_error('confirm_new_password', "Mot de passe de confirmation réquis.")
				if not bool(current_password) : self.add_error('current_password', "Mot de passe actuelle réquis.")
				return super().clean();
			else :
				if confirm_new_password == current_password :
					self.add_error('new_password', "Le nouveau mot de passe doit être différent du mot de passe actuelle.")
					return super().clean();
				else :
					user_current_password = self.user.password
					if not check_password(current_password, user_current_password) :
						raise ValidationError("Votre mot de passe actuelle est éronné.")
		return current_password
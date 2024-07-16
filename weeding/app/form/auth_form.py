from django import forms

from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError

class register(forms.Form):
	# def __init__(self, *args, **kwargs):
	# 	super().__init__(*args, **kwargs)
	# 	for field_name, field in self.fields.items():
	# 		if field.required:
	# 			field.error_messages['required'] = f"Veuillez entrer {field.label}."
	lastname = forms.CharField(label="Nom", max_length=50)
	firstname = forms.CharField(label="Prénom", max_length=50)
	middlename = forms.CharField(label="Postnom", required=False, max_length=50)
	
	nationality = forms.ChoiceField(label="Nationalité", choices=[
		('0', 'Congolaise'),
		('1', 'Canadienne'),
		('2', 'Américaine'),
		('3', 'Suisse'),
		('4', 'Russe'),
	])
	
	email = forms.EmailField(label="Email")
	phone_number = forms.CharField(label="Numéro de téléphone", required=False, validators=[RegexValidator(r'^(\s+)?(((\+243|0)9[7-9][0-9]{7})|9[7-9][0-9]{7})(\s+)?$', 'Numéro de téléphone invalide.')])
	
	sex = forms.ChoiceField(label="Sexe", choices=[('f', 'Femme'), ('m', 'Homme')])

	password = forms.CharField(label="Mot de passe", widget=forms.PasswordInput, max_length=50)
	confirm_password = forms.CharField(label="Confirmer le mot de passe", widget=forms.PasswordInput, max_length=20)
	
	def clean_confirm_password(self):
		confirm_password = self.cleaned_data.get("confirm_password")
		password = self.cleaned_data.get("password")
		if password != confirm_password :
			raise ValidationError("Le mot de passe de confirmation doit être identique au mot de passe.")
		return confirm_password


class login(forms.Form):
	email = forms.EmailField(label="Email")
	password = forms.CharField(label="Mot de passe", widget=forms.PasswordInput, max_length=50)


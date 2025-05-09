from django.apps import apps

from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import PermissionsMixin
from app.models.Person import Person

from django.utils import timezone
from django.utils.translation import gettext_lazy as _

class UserManager(BaseUserManager):
	use_in_migrations = True

	# def _create_user(self, username, email, password, **extra_fields):
	def _create_user(self, email, password, person, **extra_fields):
		"""
		Create and save a user with the given username, email, and password.
		"""
		# gbt---
			# if not username:
			# 	raise ValueError("The given username must be set")
		email = self.normalize_email(email)
		# Lookup the real model class from the global app registry so this
		# manager method can be used in migrations. This is fine because
		# managers are by definition working on the real model.
		GlobalUserModel = apps.get_model(
			self.model._meta.app_label, self.model._meta.object_name
		)
		# gbt---
			# username = GlobalUserModel.normalize_username(username)
			# user = self.model(username=username, email=email, **extra_fields)
		user = self.model(email=email, **extra_fields)
		user.password = make_password(password)
		user.person = person
		user.save(using=self._db)
		return user

	# def create_user(self, username, email=None, password=None, **extra_fields):
	def create_user(self, email=None, password=None, person=None, **extra_fields):
		extra_fields.setdefault("is_staff", False)
		extra_fields.setdefault("is_superuser", False)
		# return self._create_user(username, email, password, **extra_fields)
		return self._create_user(email, password, person, **extra_fields)

	# def create_superuser(self, username, email=None, password=None, **extra_fields):
	def create_superuser(self, email=None, password=None, person=None, **extra_fields):
		extra_fields.setdefault("is_staff", True)
		extra_fields.setdefault("is_superuser", True)

		if extra_fields.get("is_staff") is not True:
			raise ValueError("Superuser must have is_staff=True.")
		if extra_fields.get("is_superuser") is not True:
			raise ValueError("Superuser must have is_superuser=True.")

		# return self._create_user(username, email, password, **extra_fields)
		return self._create_user(email, password, person, **extra_fields)

	def with_perm(
		self, perm, is_active=True, include_superusers=True, backend=None, obj=None
	):
		if backend is None:
			backends = auth._get_backends(return_tuples=True)
			if len(backends) == 1:
				backend, _ = backends[0]
			else:
				raise ValueError(
					"You have multiple authentication backends configured and "
					"therefore must provide the `backend` argument."
				)
		elif not isinstance(backend, str):
			raise TypeError(
				"backend must be a dotted import path string (got %r)." % backend
			)
		else:
			backend = auth.load_backend(backend)
		if hasattr(backend, "with_perm"):
			return backend.with_perm(
				perm,
				is_active=is_active,
				include_superusers=include_superusers,
				obj=obj,
			)
		return self.none()
class AbstractUser(AbstractBaseUser, PermissionsMixin):
	"""
	An abstract base class implementing a fully featured User model with
	admin-compliant permissions.

	Username and password are required. Other fields are optional.
	"""

	# gbt---
		# username_validator = UnicodeUsernameValidator()

		# username = models.CharField(
		# 	_("username"),
		# 	max_length=150,
		# 	unique=True,
		# 	help_text=_(
		# 		"Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only."
		# 	),
		# 	validators=[username_validator],
		# 	error_messages={
		# 		"unique": _("A user with that username already exists."),
		# 	},
		# )
		# first_name = models.CharField(_("first name"), max_length=150, blank=True)
		# last_name = models.CharField(_("last name"), max_length=150, blank=True)
	email = models.EmailField(_("email address"), unique=True)
	is_staff = models.BooleanField(
		_("staff status"),
		default=False,
		help_text=_("Designates whether the user can log into this admin site."),
	)
	is_active = models.BooleanField(
		_("active"),
		default=True,
		help_text=_(
			"Designates whether this user should be treated as active. "
			"Unselect this instead of deleting accounts."
		),
	)
	date_joined = models.DateTimeField(_("date joined"), default=timezone.now)

	objects = UserManager()

	EMAIL_FIELD = "email"
	# gbt---
		#  USERNAME_FIELD = "username"
	USERNAME_FIELD = "email"
	REQUIRED_FIELDS = []

	class Meta:
		verbose_name = _("user")
		verbose_name_plural = _("users")
		abstract = True

	def clean(self):
		super().clean()
		self.email = self.__class__.objects.normalize_email(self.email)

	def email_user(self, subject, message, from_email=None, **kwargs):
		"""Send an email to this user."""
		send_mail(subject, message, from_email, [self.email], **kwargs)

class User(AbstractUser):
	person = models.OneToOneField(Person, on_delete = models.CASCADE, unique = True, null = True)
	# first_name = None
	# last_name = None
	# username = None

	# EMAIL_FIELD = "email"
	# USERNAME_FIELD = None
	# # REQUIRED_FIELDS = ["email"]

	class Meta():
		swappable = "AUTH_USER_MODEL"

from django.http import HttpResponse
from django.shortcuts import redirect

from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

from django.views.generic import View
from django.views.generic.base import TemplateView

from django.contrib import messages
from django.contrib.auth import login as auth_login, logout as auth_logout, authenticate

from app.models.Person import Person
from app.models.User import User

from app.form import auth_form

class register(TemplateView) :
	template_name = "app/inscription.html"
	
	form_class = auth_form.register
	register_auth_redirect = '/'
	register_save_redirect = '/'
	register_fall_redirect = '/login'

	def get_context_data(self, **kwargs):
		datas = {}
		context = {**super().get_context_data(**kwargs), **datas}
		return context
	def post(self, request, *args, **kwargs):
		form = self.form_class(request.POST)
		if form.is_valid() :
			person = Person(lastname=form.cleaned_data['lastname'], firstname=form.cleaned_data['firstname'], middlename=form.cleaned_data['middlename'], nationality=form.cleaned_data['nationality'], phone_number=form.cleaned_data['phone_number'], sex=form.cleaned_data['sex'], date_of_birth=form.cleaned_data['date_of_birth'], place_of_birth=form.cleaned_data['place_of_birth'])
			person.save()
			user = User.objects.create_user(email=form.cleaned_data['email'], password=form.cleaned_data['password'], person=person)
			user.save()
			auth_login(request, user)
			_next = request.GET.get('next')
			return redirect(_next if bool(_next) else self.register_save_redirect)
		else :
			messages.error(request, form.errors)
			return redirect(self.register_fall_redirect) if request.META.get('HTTP_REFERER', '/') == '/' else redirect(request.META.get('HTTP_REFERER', '/')) 
	def get(self, request, *args, **kwargs):
		return super().get(request, *args, **kwargs)
	def dispatch(self, *args, **kwargs):
		# Dans le futur, remplacer la ligne suivante par un décorateur Middleware(décorateur 
			# ayant pour but de n'autorisé que les non-authentifié) Custom...
		if self.request.user.is_authenticated : return redirect(self.register_auth_redirect)
		return super().dispatch(*args, **kwargs)

class login(TemplateView) :
	template_name = "app/connexion.html"
	
	form_class = auth_form.login
	login_auth_redirect = '/'
	login_fall_redirect = '/login'

	def get_context_data(self, **kwargs):
		_next = self.request.GET.get('next')
		datas = {'next_after_login' : ('?next='+_next) if _next != '' and _next != None else ''}
		context = {**super().get_context_data(**kwargs), **datas}
		return context
	def post(self, request, *args, **kwargs):
		form = self.form_class(request.POST)
		if form.is_valid() :
			user = authenticate(request, email=form.cleaned_data['email'], password=form.cleaned_data['password'])
			if user is not None :
				auth_login(request, user)
				_next = request.GET.get('next')
				return redirect(_next if bool(_next) else self.login_auth_redirect)
			else :
				form.add_error(None, 'Email ou mot de passe invalide.')
		messages.error(request, form.errors)
		return redirect(self.login_fall_redirect) if request.META.get('HTTP_REFERER', '/') == '/' else redirect(request.META.get('HTTP_REFERER', '/'))
	def get(self, request, *args, **kwargs):
		return super().get(request, *args, **kwargs)
	def dispatch(self, *args, **kwargs):
		# Dans le futur, remplacer la ligne suivante par un décorateur Middleware(décorateur 
			# ayant pour but de n'autorisé que les non-authentifié) Custom...
		if self.request.user.is_authenticated : return redirect(self.login_auth_redirect)
		return super().dispatch(*args, **kwargs)












	
@method_decorator(login_required(login_url='/login'), name='dispatch') # sur `dispatch` : pour toutes les méthode(post, get, ...) HTTP
class logout(View) :
	redirect_to = '/'
	def dispatch(self, *args, **kwargs):
		auth_logout(self.request)
		return redirect(self.redirect_to)

# class testons(TemplateView) :
# 	template_name = "auth.html"
# 	def get_context_data(self, **kwargs):
# 		datas = {}
# 		context = {**super().get_context_data(**kwargs), **datas}
# 		return context
# 	def get(self, request, *args, **kwargs):
# 		return super().get(request, *args, **kwargs)
# 	def dispatch(self, *args, **kwargs):
# 		# Dans le futur, remplacer la ligne suivante par un décorateur Middleware(décorateur 
# 			# ayant pour but de n'autorisé que les non-authentifié) Custom...
# 		if self.request.user.is_authenticated : return redirect(self.login_auth_redirect)
# 		return super().dispatch(*args, **kwargs)
from django.http import HttpResponse
from django.shortcuts import redirect

from django.utils.decorators import method_decorator
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password

from django.views.generic import View
from django.views.generic.base import TemplateView

from django.contrib import messages

from app.models.Person import Person
from app.models.User import User

from app.form import profile_form

@method_decorator(login_required(login_url='/login'), name='dispatch') # sur `dispatch` : pour toutes les méthode(post, get, ...) HTTP
class update(TemplateView) :
	template_name = "auth.html"
	update_save_redirect = None
	update_fall_redirect = '/profile/update'
	form_class = profile_form.update
	def get_context_data(self, **kwargs):
		datas = {}
		context = {**super().get_context_data(**kwargs), **datas}
		return context
	def post(self, request, *args, **kwargs):
		_next = request.GET.get('next')
		update_save_redirect = _next if bool(_next) else (request.META.get('HTTP_REFERER', '/') if self.update_save_redirect is None else self.update_save_redirect)
		user = request.user
		form = self.form_class(request.POST, id_user=user.id)
		if form.is_valid() :
			cleaned_data = form.cleaned_data
			filtered_data = {}
			updated = {}
			person = user.person
			user_is_update = False
			person_is_update = False
			update_session = False
			for attribute_name, new_value in cleaned_data.items():
				if attribute_name == 'current_password' or attribute_name == 'confirm_new_password' or (attribute_name == 'new_password' and form.cleaned_data['new_password'] == '') : continue
				elif attribute_name == 'new_password' :
					attribute_name = 'password'
					new_value = make_password(new_value)
				if new_value or form.fields[attribute_name].required:
					model = user
					current_value = getattr(model, attribute_name, None)
					if current_value == None :
						model = person
						current_value = getattr(model, attribute_name, None)
					if model is not None and (current_value != new_value) :
						if model is person : person_is_update = True
						else :
							if attribute_name == 'password' : update_session = True
							user_is_update = True
						setattr(model, attribute_name, new_value)
						updated[attribute_name] = new_value
						continue
			if person_is_update : person.save()
			if user_is_update :
				user.save()
				if update_session : update_session_auth_hash(request, user)
			messages.success(request, updated)
			return redirect(update_save_redirect)
		messages.error(request, form.errors)
		return redirect(self.update_fall_redirect) if request.META.get('HTTP_REFERER', '/') == '/' else redirect(request.META.get('HTTP_REFERER', '/'))
	def get(self, request, *args, **kwargs):
		return super().get(request, *args, **kwargs)
	def dispatch(self, *args, **kwargs):
		return super().dispatch(*args, **kwargs)

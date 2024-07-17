from django.shortcuts import render
from django.http import HttpResponse

from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

from django.views.generic.base import TemplateView

# def dashboard(request):
   
#     return render(request, 'app/dashboard.html')



@method_decorator(login_required(login_url='/login'), name='dispatch') # sur `dispatch` : pour toutes les méthode HTTP(post, get, ...)
class index(TemplateView) :
    template_name = "app/dashboard.html"
    def get_context_data(self, **kwargs):
        datas = {}
        context = {**super().get_context_data(**kwargs), **datas}
        return context
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)
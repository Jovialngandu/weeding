from app.models.Person import Person
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.views.generic import TemplateView


class testView(TemplateView):
    template_name = "app/test.html"
    def get_queryset(self):
        self.text= get_object_or_404(Person, id=1)
        return Person.objects.all()
    # def get_queryset(self):
    #     self.publisher = get_object_or_404(Publisher, name=self.kwargs["publisher"])
    #     return Book.objects.filter(publisher=self.publisher)
    def get_context_data(self, **kwargs):
    # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in the publisher
        context["hello"] = self.get_queryset()
        return context
    def post(self, request, *args, **kwargs):
		
		    return HttpResponse(request)
#    def get(self, request, *args, **kwargs):
# 		    return super().get(request, *args, **kwargs)
# 	def dispatch(self, *args, **kwargs):
		
# 		    return super().dispatch(*args, **kwargs)
    
    
    
# def test(request):

#     allpatient=Personne.objects.all()
#     allpatient2=Couple.objects.all()

#     print(allpatient2[0].personne1.nom,allpatient2[0].personne2.nom)

#     return render(request, 'app/profil.html')
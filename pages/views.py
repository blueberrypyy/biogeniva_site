from django.shortcuts import render
from django.views.generic.base import View, TemplateView

class HomePageView(TemplateView):
    template_name = 'home.html'
    #def get(self, request, *args, **kwargs):
        #return render(request, 'home.html')

class AboutPageView(TemplateView):
    template_name = 'about.html'


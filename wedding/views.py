from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from django.shortcuts import render

# Create your views here.


class WeddingHomeView(TemplateView):
     template_name = 'wedding/wedding.html'
    # def get_object(self):
    #     return self.request.user

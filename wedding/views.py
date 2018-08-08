from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, FormView, DetailView, View
from django.shortcuts import render

# Create your views here.


class WeddingHomeView(LoginRequiredMixin, DetailView):
    # template_name = 'accounts/home.html'
    # def get_object(self):
    #     return self.request.user
    pass

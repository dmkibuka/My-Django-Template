from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView, CreateView, ListView, DetailView
from django.shortcuts import render

from .forms import EventRsvpForm

# Create your views here.


class WeddingHomeView(TemplateView):
     template_name = 'wedding/wedding.html'
    # def get_object(self):
    #     return self.request.user

class EventRsvpView(CreateView):
	form_class = EventRsvpForm
	template_name = 'wedding/rsvp.html'

class WeddingGalleryListView(ListView):
	pass

class WeddingGalleryDetailView(DetailView):
	pass

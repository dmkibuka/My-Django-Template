from django.urls import path

from .views import WeddingHomeView, EventRsvpView

app_name = 'wedding'

urlpatterns = [

	path('', WeddingHomeView.as_view(), name='home'),
	path('rsvp/', EventRsvpView.as_view(), name='rsvp'),
]

from django.urls import path

from .views import WeddingHomeView, EventRsvpView, WeddingGalleryListView, WeddingGalleryDetailView

app_name = 'wedding'

urlpatterns = [

	path('', WeddingHomeView.as_view(), name='home'),
	path('rsvp/', EventRsvpView.as_view(), name='rsvp'),
	path('gallery/', WeddingGalleryListView.as_view(), name='list-gallery'),
	path('gallery/', WeddingGalleryDetailView.as_view(), name='detail-gallery'),

]

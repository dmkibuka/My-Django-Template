from django.urls import path
from photologue.views import GalleryListView, GalleryDetailView, PhotoListView, PhotoDetailView

app_name = "gallery"

urlpatterns = [
	path('', GalleryListView.as_view(), name='gallery-list'),
	path('<slug:slug>/', GalleryDetailView.as_view(), name='gallery-detail'),
	path('photolist/', PhotoListView.as_view(), name='gallery-photo-list'),
	path('photo/<slug:slug>/', PhotoDetailView.as_view(), name='gallery-photo-detail'),

]


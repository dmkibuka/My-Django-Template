from django.urls import path

from .views import WeddingHomeView

app_name = 'wedding'

urlpatterns = [

	path('', WeddingHomeView.as_view(), name='home'),

]

from django.forms import ModelForm
from django.conf import settings

User = settings.AUTH_USER_MODEL

from .models import EventRsvp


class EventRsvpForm(ModelForm):
    class Meta:
        model = EventRsvp
        fields = ['event', 'guest']


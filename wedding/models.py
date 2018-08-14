from django.db import models
from django.conf import settings

User = settings.AUTH_USER_MODEL

EVENT_CHOICES = (
	('Church Service', 'Church Service'),
	('Bachelor Party', 'Bachelor Party'),
    ('Bachelorette Party', 'Bachelorette Party'),
    ('Bridal Shower', 'Bridal Shower'),
    ('Reception', 'Reception'),
)

GUEST_CHOICES = (
	('00', '00'),
	('01', '01'),
    ('02', '02'),
    ('03', '03'),
    ('04', '04'),
    ('05', '05'),
)

class EventRsvp(models.Model):
	User 		= models.ForeignKey(User, on_delete=models.CASCADE)
	event 		= models.CharField(max_length=20, choices=EVENT_CHOICES, default='Church Service')
	guest 		= models.CharField(max_length=2, choices=GUEST_CHOICES, default='00')
	timestamp 	= models.DateTimeField(auto_now_add=True)

	class Meta:
	    verbose_name = "Event Rsvp"
	    verbose_name_plural = "Events Rsvp"

	def __str__(self):
	    return self.user.full_name

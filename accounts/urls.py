from django.urls import path, re_path
from django.contrib.auth.views import LogoutView

from .views import (
                LoginView,
                RegisterView,
                GuestRegisterView,
                AccountHomeView,
                AccountEmailActivateView,
                UserDetailUpdateView,
            )
app_name = 'accounts'

urlpatterns = [
    path('', AccountHomeView.as_view(), name='home'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
    path('register/guest/', GuestRegisterView.as_view(), name='guest_register'),
    #re_path(r'^email/confirm/(?P<key>[0-9A-Za-z]+)/$', AccountEmailActivateView.as_view(), name='email-activate'),
    path('email/confirm/<key>/', AccountEmailActivateView.as_view(), name='email-activate'),
    path('email/resend-activation/', AccountEmailActivateView.as_view(), name='resend-activation'),
    path('details/', UserDetailUpdateView.as_view(), name='user-update'),
    
]

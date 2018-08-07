from django.urls import path
from django.contrib.auth import views as auth_views

app_name = "accounts"

urlpatterns  = [
    path('password/change/',
            auth_views.PasswordChangeView.as_view(),
            name='password_change'),
    path('password/change/done/',
            auth_views.PasswordChangeDoneView.as_view(),
            name='password_change_done'),
    path('password/reset/',
            auth_views.PasswordResetView.as_view(),
            name='password_reset'),
    path('password/reset/done/',
            auth_views.PasswordResetDoneView.as_view(),
            name='password_reset_done'),
    path('password/reset/<uidb64>/<token>/',
            auth_views.PasswordResetConfirmView.as_view(),
            name='password_reset_confirm'),

    path('password/reset/complete/',
            auth_views.PasswordResetCompleteView.as_view(),
            name='password_reset_complete'),
]

# accounts/login/ [name='login']
# accounts/logout/ [name='logout']
# accounts/password_change/ [name='password_change']
# accounts/password_change/done/ [name='password_change_done']
# accounts/password_reset/ [name='password_reset']
# accounts/password_reset/done/ [name='password_reset_done']
# accounts/reset/<uidb64>/<token>/ [name='password_reset_confirm']
# accounts/reset/done/ [name='password_reset_complete']

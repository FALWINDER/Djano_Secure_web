from django.urls import path, include
from .views import redirect_to_login

urlpatterns = [
    path('', redirect_to_login),
    path('auth/', include('users.urls')),
    path('dashboard/', include('events.urls')),
    path('events/', include('registrations.urls')),
]

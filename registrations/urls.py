from django.urls import path
from .views import register_for_event, view_registered_events

urlpatterns = [
    path('register/<int:event_id>/', register_for_event, name='register_for_event'),
    path('my-registrations/', view_registered_events, name='view_registered_events'),
]

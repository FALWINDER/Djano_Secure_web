from django.shortcuts import redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from events.models import Event
from .models import Registration
from django.shortcuts import render

@login_required
def register_for_event(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    # Check if already registered
    if not Registration.objects.filter(user=request.user, event=event).exists():
        Registration.objects.create(user=request.user, event=event)
    return redirect('user_dashboard')

@login_required
def view_registered_events(request):
    registrations = Registration.objects.filter(user=request.user).select_related('event')
    return render(request, 'registrations/registered_events.html', {'registrations': registrations})

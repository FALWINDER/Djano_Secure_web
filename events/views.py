from django.shortcuts import render, redirect, get_object_or_404
from .models import Event
from django.contrib.auth.decorators import login_required
from .forms import EventForm
from registrations.models import Registration
from django.db.models import Count


@login_required
def user_dashboard(request):
    registered_event_ids = Registration.objects.filter(user=request.user).values_list('event_id', flat=True)
    events = Event.objects.exclude(id__in=registered_event_ids)
    return render(request, 'events/user_dashboard.html', {'events': events})


@login_required
def admin_dashboard(request):
    if request.user.role != 'admin':
        return redirect('user_dashboard')

    events = Event.objects.filter(created_by=request.user)\
                .annotate(registration_count=Count('registration'))
    return render(request, 'events/admin_dashboard.html', {'events': events})


@login_required
def add_event(request):
    if request.user.role != 'admin':
        return redirect('user_dashboard')

    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            event = form.save(commit=False)
            event.created_by = request.user
            event.save()
            return redirect('admin_dashboard')
    else:
        form = EventForm()
    return render(request, 'events/add_event.html', {'form': form})


@login_required
def edit_event(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    if request.user != event.created_by:
        return redirect('admin_dashboard')

    if request.method == 'POST':
        form = EventForm(request.POST, instance=event)
        if form.is_valid():
            form.save()
            return redirect('admin_dashboard')
    else:
        form = EventForm(instance=event)
    return render(request, 'events/edit_event.html', {'form': form})


@login_required
def delete_event(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    if request.user == event.created_by:
        event.delete()
    return redirect('admin_dashboard')

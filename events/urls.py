from django.urls import path
from .views import user_dashboard, admin_dashboard, add_event, edit_event, delete_event

urlpatterns = [
    path('user-dashboard/', user_dashboard, name='user_dashboard'),
    path('admin-dashboard/', admin_dashboard, name='admin_dashboard'),
    path('add/', add_event, name='add_event'),
    path('edit/<int:event_id>/', edit_event, name='edit_event'),
    path('delete/<int:event_id>/', delete_event, name='delete_event'),
]

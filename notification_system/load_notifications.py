from django.core.management import call_command
from notifications.models import Notification
def load_fixtures():
    if not Notification.objects.all():
        call_command('loaddata', 'notifications.json', app_label='notifications')

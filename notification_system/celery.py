import os
from celery import Celery
from kombu import Exchange, Queue

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'notification_system.settings')

celery_app = Celery('notification_system')
celery_app.config_from_object('django.conf:settings', namespace='CELERY')
celery_app.autodiscover_tasks()
celery_app.conf.task_queues = [
    Queue('tasks', Exchange('tasks'), routing_key='tasks', priority=1,
          queue_arguments={'priority': 10}),
    Queue('tasks2', Exchange('tasks2'), routing_key='tasks2', priority=10,
          queue_arguments={'priority': 1}),
]

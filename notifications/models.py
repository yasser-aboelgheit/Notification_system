from django.db import models


class Notification(models.Model):
    PUSH_NOTIFICATION = 0
    SMS_NOTIFICATION = 1
    BOTH = 2

    NOTIFICATION_TYPE_CHOICES = (
        (PUSH_NOTIFICATION, 'push_notification'),
        (SMS_NOTIFICATION, 'sms_notification'),
        (BOTH, 'both'),
    )
    name = models.CharField(max_length=255)
    text_en = models.TextField(null=True, blank=True)
    text_ar = models.TextField(null=True, blank=True)
    notification_type = models.IntegerField(
        choices=NOTIFICATION_TYPE_CHOICES, default=0)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

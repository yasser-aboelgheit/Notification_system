
import time
import logging
from celery import shared_task
from accounts.models import Passenger
from .models import Notification
logger = logging.getLogger('notify_logger')

@shared_task(rate_limit='10/m', max_retries=3)
def send_sms_on_promo(promo_code, expire_at, passenger_id):
    notification = Notification.objects.get(name="promo")
    passengers = Passenger.objects.all()
    notification_text_en = notification.text_en.replace("PROMO_CODE",promo_code).replace("DATE",expire_at)
    notification_text_ar = notification.text_ar.replace("رمز-دعائي",promo_code).replace("التاريخ",expire_at)
    passenger = Passenger.objects.get(id=passenger_id)
    if passenger.notification_langauge is Passenger.ENGLISH:
        logger.info("<PROMO sent to %s> %s" % (passenger.phone_number, notification_text_en))
        return True
    logger.info("<PROMO sent to %s> %s" % (passenger.phone_number, notification_text_ar))
    return True
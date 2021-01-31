
import time

from celery import shared_task
from .models import Passenger
import logging
logger = logging.getLogger('notify_logger')

@shared_task(rate_limit='10/m', max_retries=3)
def send_sms_on_register(passenger_name, phone_number):
    time.sleep(20)
    logger.info("<SMS sent to %s> Dear %s, Welcome to SWVL!" % (phone_number, passenger_name))
    return True
    
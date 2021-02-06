import json
import simplejson
from rest_framework.test import APITestCase
from accounts.factories import PassengerFactory, UserFactory
from django.urls import reverse
from django.test import TestCase
from .celery_tasks import send_sms_on_promo
from django.contrib.auth.models import User
from .models import Notification


class TestPassengerAPIView(APITestCase):
    def setUp(self):
        self.login_credentials = {
            'username': 'test1', 'password': 'testpassword'}
        User.objects.create_user(
            **self.login_credentials)
        self.url = reverse('promo_codes')
        self.login_url = reverse('token_obtain_pair')
        login_response = self.client.post(
            self.login_url, self.login_credentials)
        token = login_response.data.get("access")
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + token)
        self.body = {"promo_code": "SWVL2010",
                     "expire_at": "27/2/2021"}

    def test_successful_return(self):
        response = self.client.post(self.url, self.body)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data.get("message"),
                         "Promo codes will be sent to all users")

    def test_no_promo_code(self):
        self.body.pop("promo_code")
        response = self.client.post(self.url, self.body)
        self.assertEqual(response.status_code, 400)
        self.assertEqual(json.dumps(response.data),
                         '{"promo_code": ["This field is required."]}')

    def test_no_expire_at(self):
        self.body.pop("expire_at")
        response = self.client.post(self.url, self.body)
        self.assertEqual(response.status_code, 400)
        self.assertEqual(json.dumps(response.data),
                         '{"expire_at": ["This field is required."]}')


class TestSendSmsOnPromo(TestCase):
    def setUp(self):
        self.promo_code = "Test-Promo"
        self.expire_at = "2021-2-27"
        self.passenger = PassengerFactory.create()
        self.notification = Notification.objects.get(name="promo")
        self.notification_text_en = self.notification.text_en.replace(
            "PROMO_CODE", self.promo_code).replace("DATE", self.expire_at)
        self.notification_text_ar = self.notification.text_ar.replace(
            "رمز-دعائي", self.promo_code).replace("التاريخ", self.expire_at)

    def test_response(self):
        celery_task = send_sms_on_promo(
            self.promo_code, self.expire_at, self.passenger.id)
        self.assertEqual(celery_task, True)

    def test_notification_saved_records(self):
        self.assertEqual(
            self.notification_text_en, "Now you can use the promo code Test-Promo. valid until 2021-2-27")

    def test_sms(self):
        with open('debug.log', 'r') as f:
            lines = f.read().splitlines()
            matching = [s for s in lines if "Test-Promo" in s]
            self.assertEqual(matching[-1], "<PROMO sent to %s> %s" % (
                self.passenger.phone_number, self.notification_text_en))

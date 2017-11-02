from django.contrib.auth.models import User
from django.core import mail
from django.test import TestCase
from hc.api.models import Check
from hc.test import BaseTestCase


class LogoutTestCase(BaseTestCase):

    def test_it_logs_out_users(self):
        form = {'email': 'alice@example.org', 'password': 'password'}
        # make sure a user is logged in successfully
        response = self.client.post("/accounts/login/", form)
        self.assertEquals(response.status_code, 302)
        # logout user and test it redirects to index
        r = self.client.get("/accounts/logout", follow=True)
        self.assertEqual(r.status_code, 200)
        self.assertTemplateUsed('front/welcome.html')

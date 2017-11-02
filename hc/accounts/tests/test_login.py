from django.contrib.auth.models import User
from django.core import mail
from django.test import TestCase
from hc.api.models import Check


class LoginTestCase(TestCase):

    def test_it_sends_link(self):
        check = Check()
        check.save()

        session = self.client.session
        session["welcome_code"] = str(check.code)
        session.save()

        form = {"email": "alice@example.org"}

        r = self.client.post("/accounts/login/", form)
        assert r.status_code == 302

        ### Assert that a user was created
        user = User.objects.get(email="alice@example.org")
        checks = Check.objects.all()
        self.assertEqual(user.email, 'alice@example.org')

        # And email sent
        self.assertEqual(len(mail.outbox), 1)
        self.assertEqual(mail.outbox[0].subject, 'Log in to healthchecks.io')
        ### Assert contents of the email body
        self.assertIn('To log into healthchecks.io, please open the link below:', mail.outbox[0].body)

        ### Assert that check is associated with the new user
        self.assertEqual(checks[0].user, user)

    def test_it_pops_bad_link_from_session(self):
        self.client.session["bad_link"] = True
        self.client.get("/accounts/login/")
        assert "bad_link" not in self.client.session

        ### Any other tests?
    def test_it_renders_login_on_get(self):
        r = self.client.get("/accounts/login/")
        self.assertTemplateUsed(r, 'accounts/login.html')

    def test_it_rejects_bad_credentials(self):
        form = {"email": "asdfasd@gmail.com", "password": "sdfasdf"}
        r = self.client.post('/accounts/login/', form)
        self.assertContains(r, 'Incorrect email or password.')
        self.assertEqual(r.status_code, 200)

    def test_it_logs_in(self):
         # Alice is a normal user for tests. Alice has team access enabled.
        user = User(username="alice", email="alice@example.org")
        user.set_password("password")
        user.save()

        form = {'email': 'alice@example.org', 'password': 'password'}
        r = self.client.post('/accounts/login/', form)
        self.assertEqual(r.status_code, 302)
        self.assertRedirects(r, '/checks/')

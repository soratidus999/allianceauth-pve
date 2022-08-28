from django.test import TestCase
from django.urls import reverse
from django.conf import settings

from allianceauth.tests.auth_utils import AuthUtils


class TestHooks(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.testuser = AuthUtils.create_user('aauth_testuser')
        cls.testcharacter = AuthUtils.add_main_character_2(cls.testuser, 'aauth_testchar', 2116790529)

    def test_render_hook_success(self):
        self.testuser = AuthUtils.add_permissions_to_user_by_name(['allianceauth_pve.access_pve'], self.testuser)

        self.client.force_login(self.testuser)

        response = self.client.get(reverse('allianceauth_pve:index'))
        self.assertRedirects(response, reverse('allianceauth_pve:dashboard'))

    def test_render_hook_fail(self):
        self.client.force_login(self.testuser)

        response = self.client.get(reverse('allianceauth_pve:index'))
        self.assertRedirects(response, reverse(settings.LOGIN_URL))

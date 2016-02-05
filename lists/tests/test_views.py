from django.test import TestCase
from django.core.urlresolvers import resolve

from lists.views import home_page
from lists.models import Item, User
# Create your tests here.

class HomeViewTest(TestCase):

    def test_root_url_resolves_to_home_page(self):
        page = resolve('/')
        self.assertEqual(page.func, home_page)

    def test_home_page_redirects_to_user_account(self):
        user_name = 'Test User'
        response = self.client.post(
                '/',
                data = {'user_name': 'Test User'}
        )
        self.assertRedirects(
                response,
                '/users/%s/' % user_name.replace(' ', '-').lower()
        )


class ListViewTest(TestCase):
    pass

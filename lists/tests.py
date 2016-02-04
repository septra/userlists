from django.test import TestCase
from django.core.urlresolvers import resolve

from lists.views import home_page
# Create your tests here.

class HomePageTest(TestCase):

    def test_root_url_resolves_to_home_page(self):
        page = resolve('/')
        self.assertEqual(page.func, home_page)


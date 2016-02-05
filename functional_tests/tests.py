#!/usr/bin/python
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from django.test import LiveServerTestCase

class FunctionalTest(LiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.PhantomJS()

    def tearDown(self):
        self.browser.quit()

    # Sauron lands on the home page and sees that it's a To-Do list by
    # looking at the page title and the heading.
    def test_title_and_list_in_page(self):
        self.browser.get(self.live_server_url)
        self.assertIn('To-Do', self.browser.title)

        heading = self.browser.find_element_by_tag_name('h1')
        self.assertIn('To-Do', heading.text)

    # Sauron can see that there is an input field for him to enter his name.
    # Tempted, he types in his name and finds himself at his new account
    # created specially for him.
    def test_user_prompt_on_front_page(self):
        inputbox = self.browser.find_element_by_id('user_name_input')
        self.assertEqual(
                inputbox.get_attribute('placeholder'),
                "What's your name?"
        )

        inputbox.send_keys('Sauron the Dark')
        inputbox.send_keys(Keys.ENTER)

        self.assertRegexpMatches(
                self.browser.current_url,
                '/users/sauron-the-dark/'
        )

        self.assertIn(
                'sauron-the-dark',
                self.browser.find_element_by_tag_name('body').text
        )

    # Delighted with this new effective tool to organize his thoughts,
    # Sauron gets to work and starts listing his plans for middle earth.
    def test_user_can_input_list_items(self):
        inputbox = browser.find_element_by_id('list_item_input')
        inputbox.send_keys('Need to find my ring\n')
        inputbox.send_keys('Attack Helms Deep')

        self.assertInHTML(
            '1. Attack Helms Deep',
            self.browser.find_element_by_tag_name('table')
        )

        self.assertInHTML(
            '2. Need to find my ring'
        )

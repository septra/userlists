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
        self.browser.get(self.live_server_url)
        inputbox = self.browser.find_element_by_id('id_name')
        self.assertEqual(
                inputbox.get_attribute('placeholder'),
                "Your name"
        )

        inputbox.send_keys('Sauron the Dark')
        inputbox.send_keys(Keys.ENTER)

        self.assertRegexpMatches(
                self.browser.current_url,
                '/users/sauron-the-dark/'
        )

        self.assertIn(
                'Sauron The Dark',
                self.browser.find_element_by_tag_name('body').text
        )

    # Delighted with this new effective tool to organize his thoughts,
    # Sauron gets to work and starts listing his plans for middle earth.
    def test_user_can_input_list_items(self):
        self.browser.get(self.live_server_url)
        inputbox = self.browser.find_element_by_id('id_name')
        inputbox.send_keys('Sauron the Dark\n')

        listinput = self.browser.find_element_by_id('id_item')
        listinput.send_keys('Need to find my ring\n')
        listinput = self.browser.find_element_by_id('id_item')
        listinput.send_keys('Attack Helms Deep\n')

        self.assertIn(
            '1. Need to find my ring',
            self.browser.find_element_by_tag_name('table').text
        )

        self.assertIn(
            '2. Attack Helms Deep',
            self.browser.find_element_by_tag_name('table').text
        )

    # While he is working on his list, a dark thought comes into Sauron the Dark's
    # mind. He wants to break this new tool and reforge it for reasons best know to
    # him. He starts by pressing enter on a blank field but is unsuccessful in his
    # attempt to foil the system.
    def test_validation_of_empty_inputs(self):
        self.browser.get(self.live_server_url)
        homepage_url = self.browser.current_url

        inputbox = self.browser.find_element_by_id('id_name')
        inputbox.send_keys('   \n')

        self.assertIn('required', self.browser.find_element_by_class_name('errorlist').text)
        self.assertEqual(self.browser.current_url, homepage_url)

        inputbox = self.browser.find_element_by_id('id_name')
        inputbox.send_keys('Sauron the dark\n')

        listview_url = self.browser.current_url
        inputbox = self.browser.find_element_by_id('id_item')
        inputbox.send_keys('   \n')

        self.assertIn('required', self.browser.find_element_by_class_name('errorlist').text)
        self.assertEqual(self.browser.current_url, listview_url)

    def test_implement_user_authentication(self):
        self.fail()

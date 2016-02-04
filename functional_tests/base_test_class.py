#!/usr/bin/python
from selenium import webdriver
from django.test import LiveServerTestCase
import unittest
import sys

class FunctionalTest(LiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.PhantomJS()

    def tearDown(self):
        self.browser.quit()

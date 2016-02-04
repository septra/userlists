from .base_test_class import FunctionalTest

class InitialViewTest(FunctionalTest):

    def test_title_and_list_in_page(self):
        self.browser.get(self.live_server_url)
        
        self.assertIn('To-Do', self.browser.title)
        
        heading = self.browser.find_element_by_tag_name('h1')

        self.assertIn('To-Do', heading.text)


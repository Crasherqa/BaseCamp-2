import unittest

from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.keys import Keys

from selenium_page_object.page_object import (
    GoogleSearchPage,
    GoogleSearchResultPage
)


class TestCase(unittest.TestCase):
    def setUp(self):
        self.driver = WebDriver()

    def testPageObject(self):
        self.driver.get('http://googl.com')
        search_text = 'hello world'
        words = search_text.lower().split()

        with GoogleSearchPage(self.driver) as search_page:
            search_page.search_input.value = search_text + Keys.ENTER

        with GoogleSearchResultPage(self.driver) as result_page:
            for link in result_page.found_link.get_all():
                link_text = link.text.lower()
                assert all(text in link_text for text in words)

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()

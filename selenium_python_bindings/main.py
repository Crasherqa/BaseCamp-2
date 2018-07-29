import unittest
import argparse
import sys
import selenium.webdriver as webdrivers
import functions


class TestCase(unittest.TestCase):
    def setUp(self):
        self.driver = WebDriver()

    def testBase(self):
        functions.google_search_page_test(self.driver)

        assert self.driver.find_element_by_id("lst-ib").get_attribute("value").lower() == "hello world"
        assert self.driver.current_url.startswith("https://www.google.com/"), "Incorrect page opened"

    def tearDown(self):
        self.driver.quit()


WebDriver = None

if __name__ == "__main__":
    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument('browser', nargs=1, type=str)
    parsed = arg_parser.parse_args()
    sys.argv.pop()

    WebDriver = getattr(webdrivers, parsed.browser[0].title())

    unittest.main()

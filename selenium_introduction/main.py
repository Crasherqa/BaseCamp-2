import unittest
import argparse
import time
import sys
import selenium_patterns.webdriver as webdrivers


class TestCase(unittest.TestCase):
    def setUp(self):
        self.driver = WebDriver()

    def testBase(self):
        self.driver.get('http://google.com')
        time.sleep(1)

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

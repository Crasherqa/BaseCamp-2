import unittest

from selenium.webdriver.chrome.webdriver import WebDriver


class TestCase(unittest.TestCase):
    def setUp(self):
        self.driver = WebDriver()

    def testTables(self):
        """
        http://the-internet.herokuapp.com/tables

        Click at all table headers and after that
        verify that table sorted correctly
        """

    def testKeyPress(self):
        """
        http://the-internet.herokuapp.com/key_presses

        Press on ALT, CTRL and SHIFT keys and verify
        that correct pressed key is displayed
        """

    def testHover(self):
        """
        http://the-internet.herokuapp.com/hovers

        Hover over all users and verify that after hover
        under user picture appears additional information about user
        """

    def testDragAndDrop(self):
        """
        http://the-internet.herokuapp.com/drag_and_drop

        Drag an drop block A to block B after that verify that
        block A and block B exchanged positions
        """

    def testLoginValidCredentials(self):
        """
        http://the-internet.herokuapp.com/login

        Enter correct data into username and password fields,
        click at login button, after that verify that you
        successfully login to site
        """

    def testLoginInvalidCredentials(self):
        """
        http://the-internet.herokuapp.com/login

        Enter incorrect data into username and password fields,
        click at login button, after that verify that popup message
        appears at table
        """

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()

import time

from selenium import webdriver
import unittest


from pages_POMs.account import AccountPage
from pages_POMs.login import LoginPage
from pages_POMs.main import MainPage


class TestsLogin(unittest.TestCase):

    def setUp(self) -> None:
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get('https://magento.softwaretestingboard.com/')
        self.main_page = MainPage(self.driver)
        self.login_page = LoginPage(self.driver)
        self.account_page = AccountPage(self.driver)
        self.main_page.consent_to_cookies()

    def test_successful_login(self):
        self.main_page.navigate_to_login()
        self.login_page.login("test@grr.la", "Testtest123")
        self.account_page.check_if_logged_in()

    def test_wrong_password(self):
        self.main_page.navigate_to_login()
        self.login_page.login("test@grr.la", "test1234")
        self.login_page.check_if_alert_appears()

    def test_no_password(self):
        self.main_page.navigate_to_login()
        self.login_page.login("test@grr.la", "")
        self.login_page.check_if_password_required_alert_appears()

    def test_wrong_email_format(self):
        self.main_page.navigate_to_login()
        self.login_page.login("testgrr.la", "Testtest123")
        self.login_page.check_if_email_alert_appears()

    def test_no_email_no_password(self):
        self.main_page.navigate_to_login()
        self.login_page.login("", "")
        self.login_page.check_if_email_required_alert_appears()
        self.login_page.check_if_password_required_alert_appears()

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()


import time

from selenium import webdriver
import unittest

from pages_POMs.account import AccountPage
from pages_POMs.login import LoginPage
from pages_POMs.main import MainPage
from pages_POMs.product_page import GwenDrawstringBikeShort
from pages_POMs.search_results_page import SearchResultPage


class TestsSearchProducts(unittest.TestCase):

    def setUp(self) -> None:
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get('https://magento.softwaretestingboard.com/')
        self.main_page = MainPage(self.driver)
        self.login_page = LoginPage(self.driver)
        self.account_page = AccountPage(self.driver)
        self.search_product_page = SearchResultPage(self.driver)
        self.main_page.consent_to_cookies()
        self.product_page = GwenDrawstringBikeShort(self.driver)

    def test_search_for_existing_product(self):
        self.main_page.search_item("Gwen Drawstring Bike Short")
        time.sleep(1.5)
        self.search_product_page.check_if_correct_product_found("Gwen Drawstring Bike Short")

    def test_search_for_non_existing_product(self):
        self.main_page.search_item("horseradish")
        time.sleep(1.5)
        self.search_product_page.check_if_product_not_found_message_shown()

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()



import time

from selenium import webdriver
import unittest

from pages_POMs.account import AccountPage
from pages_POMs.login import LoginPage
from pages_POMs.main import MainPage
from pages_POMs.category_more_yoga import MoreYoga
from pages_POMs.product_page import GwenDrawstringBikeShort
from pages_POMs.cart import Cart


class TestsBuyMoreYogaProducts(unittest.TestCase):

    def setUp(self) -> None:
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get('https://magento.softwaretestingboard.com/')
        self.main_page = MainPage(self.driver)
        self.login_page = LoginPage(self.driver)
        self.account_page = AccountPage(self.driver)
        self.more_yoga = MoreYoga(self.driver)
        self.product_page = GwenDrawstringBikeShort(self.driver)
        self.cart = Cart(self.driver)
        self.main_page.consent_to_cookies()

    def test_add_item_to_cart(self):
        self.main_page.navigate_to_shop_new_yoga()
        self.more_yoga.select_product()
        self.product_page.select_size()
        self.product_page.select_color()
        self.product_page.add_product_to_cart()
        self.product_page.check_if_product_correctly_added()

    def test_remove_product_from_cart(self):
        self.main_page.navigate_to_shop_new_yoga()
        self.more_yoga.select_product()
        self.product_page.select_size()
        self.product_page.select_color()
        self.product_page.select_quantity(2)
        self.product_page.add_product_to_cart()
        self.product_page.navigate_to_cart()
        time.sleep(1)
        self.cart.remove_items_from_cart()
        time.sleep(1)
        self.cart.empty_cart_message_shown()

    def test_edit_cart(self):
        self.main_page.navigate_to_shop_new_yoga()
        self.more_yoga.select_product()
        self.product_page.select_size()
        self.product_page.select_color()
        self.product_page.add_product_to_cart()
        self.product_page.navigate_to_cart()
        time.sleep(1)
        self.cart.edit_cart()
        updated_quantity = 5
        self.product_page.select_quantity(updated_quantity)
        self.product_page.update_cart()
        time.sleep(2)
        assert self.cart.get_single_product_price() * updated_quantity == self.cart.get_multiple_products_price()

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()

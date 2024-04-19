from selenium.webdriver.common.by import By

from pages_POMs.base import BasePage


class MoreYoga(BasePage):
    def __init__(self, driver):
        self.driver = driver
        self.product_link_selector = (By.CSS_SELECTOR, "a.product-item-link[href='https://magento.softwaretestingboard.com/gwen-drawstring-bike-short.html']")

    def select_product(self):
        self.driver.find_element(*self.product_link_selector).click()

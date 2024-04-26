from selenium.webdriver.common.by import By

from pages_POMs.base import BasePage


class SearchResultPage(BasePage):
    def __init__(self, driver):
        self.driver = driver
        self.product_tile = (By.CSS_SELECTOR, ".product-item-name .product-item-link")
        self.product_not_found_error = (By.XPATH, "//div[@class='message notice']")

    def check_if_correct_product_found(self, product):
        product_name = self.driver.find_element(*self.product_tile).text
        assert product_name == product

    def check_if_product_not_found_message_shown(self):
        error_message = self.driver.find_element(*self.product_not_found_error).text
        assert error_message == "Your search returned no results."


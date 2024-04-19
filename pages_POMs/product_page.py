import time
from selenium.webdriver.common.by import By

from pages_POMs.base import BasePage


class GwenDrawstringBikeShort(BasePage):
    def __init__(self, driver):
        self.driver = driver
        self.product_size_selector = (By.ID, "option-label-size-143-item-175")
        self.product_color_selector = (By.ID, "option-label-color-93-item-52")
        self.add_to_cart_button_selector = (By.ID, "product-addtocart-button")
        self.product_quantity_box = (By.ID, "qty")
        self.cart_counter_selector = (By.CLASS_NAME, "counter-number")
        self.cart_button_selector = (By.XPATH, "//a[@class='action showcart']")
        self.proceed_to_checkout_button = (By.ID, "top-cart-btn-checkout")
        self.view_edit_cart_button = (By.CSS_SELECTOR, "a.action.viewcart")
        self.update_cart_button_selector = (By.CSS_SELECTOR, "button#product-updatecart-button.action.primary.tocart")

    def select_size(self):
        self.driver.find_element(*self.product_size_selector).click()

    def select_color(self):
        self.driver.find_element(*self.product_color_selector).click()

    def select_quantity(self, quantity: int):
        self.driver.find_element(*self.product_quantity_box).clear()
        self.driver.find_element(*self.product_quantity_box).send_keys(quantity)

    def add_product_to_cart(self):
        self.driver.find_element(*self.add_to_cart_button_selector).click()
        time.sleep(3)

    def check_if_product_correctly_added(self):
        input_quantity = self.driver.find_element(*self.product_quantity_box)
        counter_element = self.driver.find_element(*self.cart_counter_selector)
        assert input_quantity.get_attribute("value") == counter_element.text

    def navigate_to_cart(self):
        self.driver.find_element(*self.cart_button_selector).click()
        time.sleep(1.5)
        self.driver.find_element(*self.view_edit_cart_button).click()

    def update_cart(self):
        self.driver.find_element(*self.update_cart_button_selector).click()




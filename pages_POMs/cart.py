from selenium.webdriver.common.by import By

from pages_POMs.base import BasePage


class Cart(BasePage):
    def __init__(self, driver):
        self.driver = driver
        self.delete_items_button = (By.CLASS_NAME, "action-delete")
        self.empty_cart_message = (By.CSS_SELECTOR, "div.cart-empty")
        self.edit_cart_button = (By.CSS_SELECTOR, "a.action.action-edit")
        self.single_item_price_selector = (By.CSS_SELECTOR, "td.col.price span.price")
        self.multiple_items_price_selector = (By.CSS_SELECTOR, "td.col.subtotal span.price")

    def remove_items_from_cart(self):
        self.driver.find_element(*self.delete_items_button).click()

    def empty_cart_message_shown(self):
        message_text = 'You have no items in your shopping cart.\nClick here to continue shopping.'
        shown_text = self.driver.find_element(*self.empty_cart_message).text
        assert message_text == shown_text

    def edit_cart(self):
        self.driver.find_element(*self.edit_cart_button).click()

    def get_single_product_price(self):
        product_price_text = self.driver.find_element(*self.single_item_price_selector)
        product_price = float(product_price_text.text[1:])
        return int(product_price)

    def get_multiple_products_price(self):
        multiple_products_price_text = self.driver.find_element(*self.multiple_items_price_selector)
        multiple_product_price = float(multiple_products_price_text.text[1:])
        return int(multiple_product_price)

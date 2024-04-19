from selenium.webdriver.common.by import By

from pages_POMs.base import BasePage


class MainPage(BasePage):
    def __init__(self, driver):
        self.driver = driver
        self.search_field_selector = (By.ID, "search")
        self.search_button_selector = (By.CLASS_NAME, "action search")
        self.sign_in_selector = (By.CSS_SELECTOR, "a[href='https://magento.softwaretestingboard.com/customer/account/login/referer/aHR0cHM6Ly9tYWdlbnRvLnNvZnR3YXJldGVzdGluZ2JvYXJkLmNvbS8%2C/']")
        self.register_selector = (By.NAME, "Create an Account")
        self.my_cart_link = (By.CLASS_NAME, "action showcart")
        self.consent_cookies_button = (By.CSS_SELECTOR, "p.fc-button-label")
        self.shop_more_yoga_button = (By.PARTIAL_LINK_TEXT, "Shop New Yoga")

    def go_to_page(self, url):
        self.driver.get(url)

    def consent_to_cookies(self):
        self.driver.find_element(*self.consent_cookies_button).click()

    def search_item(self, product):
        self.driver.find_element(*self.search_field_selector).clear()
        self.driver.find_element(*self.search_field_selector).send_keys(product)
        self.driver.find_element(*self.search_button_selector).click()

    def open_my_cart(self):
        self.driver.find_element(*self.my_cart_link).click()

    def navigate_to_login(self):
        self.driver.find_element(*self.sign_in_selector).click()

    def navigate_to_register(self):
        self.driver.find_element(*self.register_selector).click()

    def navigate_to_shop_new_yoga(self):
        self.driver.find_element(*self.shop_more_yoga_button).click()
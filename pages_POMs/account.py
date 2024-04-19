from selenium.webdriver.common.by import By

from pages_POMs.base import BasePage


class AccountPage(BasePage):
    def __init__(self, driver):
        self.driver = driver
        self.account_tab_selector = (By.CLASS_NAME, "logged-in")

    def check_if_logged_in(self):
        self.driver.find_element(*self.account_tab_selector)
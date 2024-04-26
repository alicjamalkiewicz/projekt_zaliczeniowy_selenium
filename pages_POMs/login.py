import time

from selenium.webdriver.common.by import By

from pages_POMs.base import BasePage


class LoginPage(BasePage):
    def __init__(self, driver):
        self.driver = driver
        self.email_field_selector = (By.ID, "email")
        self.password_field_selector = (By.ID, "pass")
        self.submit_button_selector = (By.ID, "send2")
        self.incorrect_login_alert_box_selector = (By.CSS_SELECTOR, "div[data-bind='html: $parent.prepareMessageForHtml(message.text)']")
        self.incorrect_email_alert_box_selector = (By.ID, "email-error")
        self.password_required_alert_box_selector = (By.ID, "pass-error")
        self.email_required_alert_box_selector =(By.XPATH, '//div[@class="mage-error" and @id="email-error"]')

    def login(self, email, password):
        self.driver.find_element(*self.email_field_selector).send_keys(email)
        self.driver.find_element(*self.password_field_selector).send_keys(password)
        self.driver.find_element(*self.submit_button_selector).click()
        time.sleep(1.5)

    def check_if_alert_appears(self):
        error_message = self.driver.find_element(*self.incorrect_login_alert_box_selector).text
        assert error_message == "The account sign-in was incorrect or your account is disabled temporarily. Please wait and try again later."

    def check_if_email_alert_appears(self):
        error_message = self.driver.find_element(*self.incorrect_email_alert_box_selector).text
        assert error_message == "Please enter a valid email address (Ex: johndoe@domain.com)."

    def check_if_password_required_alert_appears(self):
        error_message = self.driver.find_element(*self.password_required_alert_box_selector).text
        assert error_message == "This is a required field."

    def check_if_email_required_alert_appears(self):
        error_message = self.driver.find_element(*self.email_required_alert_box_selector)
        assert error_message == "This is a required field."

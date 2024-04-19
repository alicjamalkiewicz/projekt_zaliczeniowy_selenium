from selenium import webdriver


class BasePage:

    def __init__(self, driver: webdriver.Chrome):
        self.driver = driver
        self.driver.get("https://magento.softwaretestingboard.com/")

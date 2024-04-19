from selenium.webdriver.chrome import webdriver
from webdriver_manager.chrome import ChromeDriverManager

chrome_option = webdriver.Options
chrome_option.add_argument("--start-maximized")


driver = webdriver.WebDriver(ChromeDriverManager().install(), options=chrome_option)

driver.get("https://magento.softwaretestingboard.com/")
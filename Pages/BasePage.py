from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def do_click(self, locator):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.presence_of_element_located(locator)).click()

    def do_send_keys(self, locator, text):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.presence_of_element_located(locator)).send_keys(text)

    def do_get_element_text(self, locator):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.presence_of_element_located(locator))
        return element.text

    def do_get_title(self, title):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.title_is(title))
        return self.driver.title

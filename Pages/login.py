import time

from selenium.webdriver.common.by import By
from Pages.HomePage import HomePage
from Util.genericReader import get_reader
from Pages.BasePage import BasePage
from Base.config import TestData


class LoginPage(BasePage):
    USERNAME_FIELD = (By.ID, "username")
    PASSWORD_FIELD = (By.ID, "password")
    LOGIN_BTN = (By.ID, "submit")
    MESSAGE = (By.ID, "error")
    PAGE_TITLE = "Test Login | Practice Test Automation"

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(TestData.BASE_URL)

    def get_login_page_title(self, title):
        return self.do_get_title(title)

    def do_login(self, username, password):
        self.do_send_keys(self.USERNAME_FIELD, username)
        self.do_send_keys(self.PASSWORD_FIELD, password)
        time.sleep(3)
        self.do_click(self.LOGIN_BTN)
        return HomePage(self.driver)

    def reload(self):
        self.driver.refresh()

    def display_message(self, message_locator):
        text_message = self.do_get_element_text(message_locator)
        print(text_message)
        return bool(text_message)

    def do_get_screenshot(self, filename):
        self.driver.save_screenshot(filename)

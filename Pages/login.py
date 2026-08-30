from selenium.webdriver.common.by import By
from Pages.BasePage import BasePage
from Base.config import TestData


class LoginPage(BasePage):
    USERNAME_FIELD = (By.ID, "email")
    PASSWORD_FIELD = (By.ID, "password")
    LOGIN_BTN = (By.CSS_SELECTOR, "button.btn.btn-primary.btn-lg")
    MESSAGE = (By.XPATH, "//*[@id='content']/div[3]/div/div[1]/div/form/div[5]")

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(TestData.BASE_URL)

    def get_login_page_title(self, title):
        return self.do_get_title(title)

    def do_login(self, username, password):
        self.do_send_keys(self.USERNAME_FIELD, username)
        self.do_send_keys(self.PASSWORD_FIELD, password)
        self.do_click(self.LOGIN_BTN)

    def reload(self):
        self.driver.refresh()

    def display_message(self, message_locator):
        text_message = self.do_get_element_text(message_locator)
        print(text_message)
        return bool(text_message)

    def do_get_screenshot(self, filename):
        self.driver.save_screenshot(filename)

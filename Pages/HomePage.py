from selenium.webdriver.common.by import By
from Pages.BasePage import BasePage
from Base.config import TestData


class HomePage(BasePage):

    PAGE_TITLE = "Logged In Successfully | Practice Test Automation"
    PAGE_URL = "https://practicetestautomation.com/logged-in-successfully/"
    LOGOUT_BTN = (By.XPATH, "//a[text()='Log out']")

    def __init__(self, driver):
        super().__init__(driver)

    def get_home_page_title(self, title):
        return self.do_get_title(title)

    def get_home_page_url(self, url):
        return self.do_get_url(url)

    def is_logout_button_present(self):
        logout = self.do_get_element_text(self.LOGOUT_BTN)
        if logout == "Log out":
            return True
        return False

from Base.config import TestData
from Pages.login import LoginPage
from Tests.test_base import BaseTest
from Util.genericReader import GetCred
import pytest
import time


@pytest.mark.parametrize("filepath", [TestData.USERDATA_PATH_XL])
class TestHome(BaseTest):
    def test_home_page_title(self, filepath):
        self.loginPage = LoginPage(self.driver)
        self.file = GetCred(filepath)
        username, password = self.file.get_credentials(1)
        homepage = self.loginPage.do_login(username, password)
        time.sleep(3)
        title = homepage.get_home_page_title(homepage.PAGE_TITLE)
        assert title == homepage.PAGE_TITLE

    def test_home_page_url(self, filepath):
        self.loginPage = LoginPage(self.driver)
        self.file = GetCred(filepath)
        username, password = self.file.get_credentials(1)
        homepage = self.loginPage.do_login(username, password)
        time.sleep(3)
        url = homepage.get_home_page_url(homepage.PAGE_URL)
        assert url == homepage.PAGE_URL

    def test_logout_button(self, filepath):
        self.loginPage = LoginPage(self.driver)
        self.file = GetCred(filepath)
        username, password = self.file.get_credentials(1)
        homepage = self.loginPage.do_login(username, password)
        time.sleep(3)
        is_present = homepage.is_logout_button_present()
        assert is_present is True



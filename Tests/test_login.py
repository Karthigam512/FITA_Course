from Base.config import TestData
from Pages.login import LoginPage
from Tests.test_base import BaseTest
from Util.genericReader import GetCred
import pytest
import time


class TestLogin(BaseTest):

    def test_login_page_title(self):
        self.page = LoginPage(self.driver)
        flag = self.page.get_login_page_title(LoginPage.PAGE_TITLE)
        assert flag

    @pytest.mark.parametrize("filepath", [TestData.USERDATA_PATH_CSV])
    def test_valid_login(self, filepath):
        self.page = LoginPage(self.driver)
        self.file = GetCred(filepath)
        data_count = self.file.get_data_count()
        for index in range(data_count):
            username, password = self.file.get_credentials(index)
            print(f"Running test for: {username}")
            self.page.do_login(username, password)
            time.sleep(3)
            flag = self.page.display_message(LoginPage.MESSAGE)
            assert flag is True
            self.page.do_get_screenshot(f"testcase_{username}.png")
            time.sleep(2)
            self.page.reload()

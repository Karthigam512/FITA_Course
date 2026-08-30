from Base.config import TestData
from Pages.login import LoginPage
from Tests.test_base import BaseTest
from Util.genericReader import get_reader
import pytest
import time


class TestLogin(BaseTest):

    def test_driver_title(self):
        self.page = LoginPage(self.driver)
        flag = self.page.get_login_page_title(TestData.PAGE_TITLE)
        assert flag

    @pytest.mark.parametrize("filepath", [TestData.USERDATA_PATH_CSV, TestData.USERDATA_PATH_XL])
    def test_valid_login(self, filepath):
        self.page = LoginPage(self.driver)
        userdata = get_reader(filepath).read_userdata()
        print(userdata)
        for col1, col2 in userdata:
            username = col1
            password = col2
            print(f"Running test for: {username}")
            self.page.do_login(username, password)
            time.sleep(3)
            flag = self.page.display_message(LoginPage.MESSAGE)
            assert flag is True
            self.page.do_get_screenshot(f"testcase_{username}.png")
            time.sleep(2)
            self.page.reload()

from Base.config import BaseDriver
from Pages.login import LoginPage
from Util.genericReader import get_reader
import pytest
import time


class TestLogin:
    @pytest.mark.parametrize("filepath",
                             ["C:/Users/karth/Project/pythonProjectTEST/Pages/credentials.csv",
                              "C:/Users/karth/Project/pythonProjectTEST/Util/userdata.xlsx"])
    def test_valid_login(self, filepath):
        base = BaseDriver()
        driver = base.get_driver()
        login_page = LoginPage(driver)
        csv_data = get_reader(filepath).read_userdata()
        print(csv_data)
        for col1, col2 in csv_data:
            username = col1
            password = col2
            print(f"Running test for: {username}")
            login_page.enter_username(username)
            login_page.enter_password(password)
            login_page.click_login()
            time.sleep(3)
            message_xpath = "//*[@id='content']/div[3]/div/div[1]/div/form/div[5]"
            assert login_page.display_message(message_xpath) is not None
            driver.save_screenshot(f"testcase_{username}.png")
            time.sleep(2)
            login_page.reload()
        driver.quit()

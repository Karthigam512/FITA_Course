from Base.config import BaseDriver
from Pages.login import LoginPage
#from Util.readExcel import read_userdata
from Util.readExcel_2 import read_userdata
import time


class TestLogin:
    def test_valid_login(self):
        base = BaseDriver()
        driver = base.get_driver()
        login_page = LoginPage(driver)
        filepath = "C:/Users/karth/Project/pythonProjectTEST/Util/userdata.xlsx"
        row_data = read_userdata(filepath, "Login")
        print(row_data)
        for col1, col2 in row_data:
            username = col1
            password = col2
            print(f"Running test for: {username}")
            login_page.enter_username(username)
            login_page.enter_password(password)
            login_page.click_login()
            time.sleep(3)
            message_xpath = "//*[@id='content']/div[3]/div/div[1]/div/form/div[5]"
            login_page.display_message(message_xpath)
            driver.save_screenshot(f"testcase_{username}.png")
            login_page.reload()
        driver.quit()


test = TestLogin()
test.test_valid_login()

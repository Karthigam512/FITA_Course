from Base.config import BaseDriver
from Pages.login import LoginPage
from Util.csvReader import CsvRead
import time


class TestLogin:
    def test_valid_login(self):
        base = BaseDriver()
        driver = base.get_driver()
        login_page = LoginPage(driver)
        filepath = "C:/Users/karth/Project/pythonProjectTEST/Pages/credentials.csv"
        reader = CsvRead(filepath)
        csv_data = reader.read_data()
        print(csv_data)
        for data in csv_data:
            username = data["username"]
            password = data["password"]
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

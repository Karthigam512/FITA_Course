from selenium import webdriver


class BaseDriver:
    def __init__(self, browser="chrome"):
        if browser == "chrome":
            self.driver = webdriver.Chrome()
        elif browser == "firefox":
            self.driver = webdriver.Firefox()
        self.driver.maximize_window()

    def get_driver(self):
        self.driver.get("https://imeetify.com/login")
        return self.driver

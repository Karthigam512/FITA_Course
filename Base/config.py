from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService


class BaseDriver:
    def __init__(self, browser="chrome"):
        if browser == "chrome":
            _service = ChromeService(ChromeDriverManager().install())
            self.driver = webdriver.Chrome(service=_service)
        elif browser == "firefox":
            _service = FirefoxService(GeckoDriverManager().install())
            self.driver = webdriver.Firefox(service=_service)
        self.driver.maximize_window()

    def get_driver(self):
        self.driver.get("https://imeetify.com/login")
        return self.driver

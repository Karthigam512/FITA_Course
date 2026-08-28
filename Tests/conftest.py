import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService


@pytest.fixture(params=["chrome", "firefox"], scope='class')
def init_driver(request):
    if request.param == "chrome":
        _service = ChromeService(ChromeDriverManager().install())
        web_driver = webdriver.Chrome(service=_service)
    elif request.param == "firefox":
        _service = FirefoxService(GeckoDriverManager().install())
        web_driver = webdriver.Firefox(service=_service)
    request.cls.driver = web_driver
    yield
    web_driver.quit()

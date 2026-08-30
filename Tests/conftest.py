import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.firefox.options import Options


@pytest.fixture(params=["chrome", "firefox"], scope='class')
def init_driver(request):
    if request.param == "chrome":
        _service = ChromeService(ChromeDriverManager().install())
        web_driver = webdriver.Chrome(service=_service)
    elif request.param == "firefox":
        _options = Options()
        _options.add_argument("--headless")
        _options.add_argument("--window-size=1920,1080")
        _service = FirefoxService(GeckoDriverManager().install())
        web_driver = webdriver.Firefox(service=_service, options=_options)
    request.cls.driver = web_driver
    yield
    web_driver.quit()

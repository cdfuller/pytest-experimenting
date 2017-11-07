import pytest
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

BROWSERS = {
    'firefox': DesiredCapabilities.FIREFOX,
    'chrome': DesiredCapabilities.CHROME,
}

WEBDRIVER_ENDPOINT = 'http://192.168.1.19:4444/wd/hub'

@pytest.yield_fixture(params=BROWSERS.keys())
def browser(request):
    driver = webdriver.Remote(
        command_executor=WEBDRIVER_ENDPOINT,
        desired_capabilities=BROWSERS[request.param]
    )
    yield driver
    driver.quit()
import os
from datetime import datetime
import pytest
from selenium import webdriver


from webdriver_manager.chrome import ChromeDriverManager
from utilities.BaseClass import BaseClass
#from utilities.configuration import get_config
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import codecs
log = BaseClass.get_logger()
driver = None




DIR = os.path.dirname(os.path.abspath(__file__))
Project_PATH = os.path.abspath(os.path.join(DIR, os.pardir))
directory = "reports"
print(DIR , "jp",Project_PATH,"")
REPORT_PATH = os.path.join(Project_PATH, directory)
print(REPORT_PATH)

def pytest_addoption(parser):
    parser.addoption("--browser_name", action="store", default="chrome")

@pytest.fixture(scope="class")
def setup(request):

    """ This method is used for setting the driver for the session
    and closing it after the session is completed

    parameters: request is used for calling currently running driver
    so that we can close it
    """
    global driver
    browser_name = request.config.getoption("browser_name")
    if browser_name == "chrome":
        service_obj = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service_obj)

    """elif browser_name == "firefox":
        driver = webdriver.Firefox(executable_path="C:\\geckodriver.exe")
    elif browser_name == "IE":
        print("IE driver")"""

    driver.maximize_window()

    driver.get("https://www.flipkart.com/")

    driver.implicitly_wait(30)

    request.cls.driver = driver

    yield

    driver.close()


def pytest_html_report_title(report):
    """ This method is used for  setting a heading for HTMl Report """
    report.title = "Selenium_ET_Flipkart Automation"




@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):

    """ This method is used for saving Screenshots for the failed testcases and
    attach them to the report
    """
    pytest_html = item.config.pluginmanager.getplugin("html")
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, "extra", [])
    if report.when == "call":

        nodeid = item.nodeid
        xfail = hasattr(report, "wasxfail")
        if (report.skipped and xfail) or (report.failed and not xfail):
            file_name = f'{nodeid}_{datetime.today().strftime("%Y-%m-%d_%H_%M")}.png'.replace("/", "_").replace("::",
                                                                                                                "_").replace(
                ".py", "")
            img_path = os.path.join(REPORT_PATH, "screenshots", file_name)

            driver.save_screenshot(img_path)

            screenshot = driver.get_screenshot_as_base64()
            extra.append(pytest_html.extras.image(screenshot, ''))
        report.extra = extra




from selenium.webdriver import Chrome
from selenium.webdriver.chrome.service import Service
from Base import InitiateDriver
from Library import ConfigReader
from Pages import RegistrationPage
import pytest
from DataGenerate import DataGen

@pytest.fixture(scope="module")
def setPath():
    global driver
    path = r"C:\Users\Niru\Desktop\Codes\New folder\Driver\chromedriver.exe"
    driver = Chrome(service=Service(path))
    yield
    driver.close()

# Skiping a test case unconditionally.
@pytest.mark.skip("Test: skip a test case.")
def test_load_webpage_skip_unconditionally(setPath):
    driver.get("https://www.bookmundi.com")
    driver.maximize_window()

# Skiping a test case using condition.
a = 100
@pytest.mark.skipif(a>=100, reason = "Condition matched so skipping this test case." )
def test_load_webpage_skip_conditionally(setPath):
    driver.get("https://www.bookmundi.com")
    driver.maximize_window()

# Goup of test cases for Smoke/Sanity test.
@pytest.mark.Smoke
def test_load_webpage_smoke_test(setPath):
    driver.get("https://www.bookmundi.com")
    driver.maximize_window()

@pytest.mark.Sanity
def test_load_webpage_smoke_test(setPath):
    driver.get("https://www.bookmundi.com")
    driver.maximize_window()

@pytest.mark.Smoke
def test_load_webpage_smoke_test2(setPath):
    driver.get("https://www.bookmundi.com")
    driver.maximize_window()

@pytest.mark.parametrize('data',DataGen.dataGenerator())
def test_ValidateRegistration(data):
    driver = InitiateDriver.startBrowser()
    register = RegistrationPage.RegistrationClass(driver)
    register.enter_username('data[0]')
    register.enter_password('data[1]')


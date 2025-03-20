from selenium.webdriver import Chrome
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import selenium.webdriver.support.expected_conditions as EC
import time
import pytest

@pytest.fixture()
def environment_setup():
    global driver
    path = r"C:\Users\Niru\Desktop\Codes\New folder\Driver\chromedriver.exe"
    driver = Chrome(service=Service(path))
    driver.get("http://www.theTestingWorld.com/testings")
    driver.maximize_window()
    yield
    driver.close()

def test_verify_registration(environment_setup):
    driver.find_element(By.XPATH, '//label[text()="Login"]').click()
    driver.find_element(By.NAME, "_txtUserName").send_keys("tzpraadh")
    driver.find_element(By.NAME, "_txtPassword").send_keys("test")
    driver.find_element(By.XPATH, "//input[@type='submit' and @value='Login']").click()
    driver.find_element(By.XPATH, "//a[contains(text(), 'My Account')]").click()
    driver.find_element(By.XPATH, "//a[contains(text(), 'Update')]").click()
    time.sleep(5)
    allwindows = driver.window_handles
    
    mainWin=""
    for win in allwindows:
        driver.switch_to.window(win)
        if(driver.current_url=='http://www.thetestingworld.com/testings/manage_customer.php'):
            driver.find_element(By.XPATH, "//button(text()='Start Download')").click()
            time.sleep(5)
            driver.close()
        elif(driver.current_url=='http://www.thetestingworld.com/testings/dashboard.php'):
            mainWin=win

    driver.switch_to.window(win)
    print(driver.current_url)


    # wait = WebDriverWait(driver, 100)
    # wait.until(EC.text_to_be_present_in_element(By.ID, 'countryID','India'))
    # obj = Select(driver.find_element_by_id("countryId"))

    # obj.select_by_visible_text("India")

    # wait.until(EC.text_to_be_present_in_element((By.ID, 'stateId'), "Delhi"))
    # obj = Select(driver.find_element(By.ID, "stateId"))
    # obj.select_by_visible_text("Delhi")
from selenium.webdriver import Chrome
from selenium.webdriver import Firefox
from selenium.webdriver.chrome.service import Service
from Library import ConfigReader

def startBrowser():
    global driver
    if((ConfigReader.readConfigData('Details','Browser'))=="chrome"):
        path = "./Driver/chromedriver.exe"
        driver = Chrome(service=Service(path))
    elif((ConfigReader.readConfigData('Details','Browser'))=="firefox"):
        path = './Driver/geckodriver.exe'
        driver = Firefox(service=Service(path))
    else:
        path = r"C:\Users\Niru\Desktop\Codes\New folder\chromedriver_win32\chromedriver.exe"
        driver=Chrome(service=Service(path))

    driver.get(ConfigReader.readConfigData('Details','Application_URL'))
    driver.maximize_window()
    return driver

def closeBrowser():
    driver.close()
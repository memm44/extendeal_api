from selenium.webdriver import Chrome, DesiredCapabilities
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def get_chrome_driver_local(headless=False):
    opt = Options()
    if headless:
        opt.add_argument("--headless")
    return Chrome(executable_path=r'C:\Users\Miguel\PycharmProjects\extendeal\src\driver\chromedriver.exe', options=opt)


def get_chrome_driver_docker():
    browser = webdriver.Remote(
        command_executor='http://chrome:4444/wd/hub',
        desired_capabilities=DesiredCapabilities.CHROME)
    return browser

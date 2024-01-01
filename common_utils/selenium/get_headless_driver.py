from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium import webdriver

def get_headless_driver():
    chrome_driver = '/Users/wingatejones/Downloads/chromedriver-mac-arm64/chromedriver'
    service = Service(chrome_driver)
    chrome_options = Options()
    chrome_options.add_argument("--headless=new") # for Chrome >= 109
    driver = webdriver.Chrome(service=service, options=chrome_options)
    return driver


# Created by Shark at 11.02.2020
from selenium.webdriver.chrome.webdriver import WebDriver


def test_motodom_login():
    driver = WebDriver(executable_path='C://chromedriver.exe')
    driver.get('https://motodom.com.ua/index.php?route=account/login')
    driver.implicitly_wait(3)
    search_login = driver.find_element_by_xpath('//input[@id="input-email"]')
    search_password = driver.find_element_by_xpath('//input[@id="input-password"]')
    search_button_login = driver.find_element_by_xpath("//input[@type='submit']")
    search_login.send_keys("volosorgua@gmail.com")
    search_password.send_keys("123456789")
    search_button_login.click()
    assert driver.find_element_by_xpath("//div[@class='content my-account']")

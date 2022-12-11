# Created by Shark at 11.02.2020
from selenium import webdriver
import allure
from selenium.webdriver.chrome import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

from test_add_to_cart import driver


def test_motodom_login():
    #driver_service = Service(executable_path='C://chromedriver.exe')
    #driver = webdriver.Chrome(service=driver_service)
    driver.get('https://motodom.ua/index.php?route=account/login')
    driver.implicitly_wait(3)
    search_login = driver.find_element(By.XPATH, '//input[@id="input-email"]')
    search_password = driver.find_element(By.XPATH, '//input[@id="input-password"]')
    search_button_login = driver.find_element(By.XPATH, "//button[@type='submit']")
    search_login.send_keys("volosorgua@gmail.com")
    search_password.send_keys("123456789")
    search_button_login.click()
    assert driver.find_element(By.XPATH, "//div[@class='my-account']")

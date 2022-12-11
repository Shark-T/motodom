# Created by Shark at 11.02.2020
import time
import allure
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


driver_service = Service(executable_path='C://chromedriver.exe')
driver = webdriver.Chrome(service=driver_service)

def test_add_to_cart():
    driver.get('https://motodom.ua')
    find_goods = driver.find_elements(By.XPATH, ".//div[@class='name']//a[contains(text(), 'Oxford')]") #[10].click()
    find_goods[0].click()
    find_name = driver.find_element(By.XPATH, ".//h1[@class]").text.lower()
    # choice_size = driver.find_elements(By.XPATH, ".//label[contains(text(), 'Размер')]//..//ul//li")
    #print(choice_size)
    #choice_size[0].click()
    choice_color = driver.find_element(By.XPATH, ".//span[@class='option-value']")
    choice_color.click()
    driver.find_element(By.XPATH, ".//a[@id='button-cart']").click()
    time.sleep(5)
    driver.find_element(By.XPATH, ".//div[@id='cart']").click()
    driver.find_element(By.XPATH, ".//a[@class='btn-cart btn']").click()
    assert find_name == driver.find_element(By.XPATH, ".//td[@class='name']//a[contains(text(), 'Подшлемник Oxford Cotton')]").text.lower()

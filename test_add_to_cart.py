# Created by Shark at 11.02.2020
from selenium.webdriver.chrome.webdriver import WebDriver
import time

def test_add_to_cart():
    driver = WebDriver(executable_path='C://chromedriver.exe')
    driver.get('https://motodom.com.ua')
    driver.find_elements_by_xpath("//div[@class='name']//a[contains(text(), 'Мотоботы')]")[2].click()
    find_name = driver.find_element_by_xpath("//h1[@class]").text
    choice_size = driver.find_elements_by_xpath(".//label[contains(text(), 'Размер')]//..//ul//li")
    choice_size[0].click()
    choice_color = driver.find_elements_by_xpath(".//label[contains(text(), 'Цвет')]//..//ul//li")
    choice_color[0].click()
    driver.find_element_by_xpath(".//button[@id='button-cart']").click()
    time.sleep(15)
    driver.find_element_by_xpath("//div[@id='cart']//button[@data-toggle='dropdown']").click()
    driver.find_element_by_xpath("//a[contains(text(), 'Открыть корзину')]").click()
    assert find_name == driver.find_element_by_xpath("//form//div//table//tbody//td[@class='text-left name']//a").text

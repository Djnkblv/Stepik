from idlelib import browser
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
import math
import os

driver = webdriver.Chrome(executable_path='chromedriver.exe')
driver.implicitly_wait(5)
driver.get('http://suninjuly.github.io/file_input.html')

first = driver.find_element_by_css_selector('input[name="firstname"]')
first.send_keys("Konstantin")
last = driver.find_element_by_css_selector('input[name="lastname"]')
last.send_keys('Djankabulov')
email = driver.find_element_by_css_selector('input[name="email"]')
email.send_keys("Djnkblv@gmail.com")

current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла
file_path = os.path.join(current_dir, 'file.txt')           # добавляем к этому пути имя файла
element = driver.find_element_by_css_selector('#file')
element.send_keys(file_path)

btn = driver.find_element_by_css_selector('button[type="submit"]')
btn.click()
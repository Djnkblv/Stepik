from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

driver = webdriver.Chrome(executable_path='chromedriver.exe')
driver.implicitly_wait(5)
driver.get('http://suninjuly.github.io/get_attribute.html')

sunduk = driver.find_element_by_id("treasure")
x_element = sunduk.get_attribute("valuex")
x = x_element
y = calc(x)


otvet = driver.find_element_by_css_selector('#answer')
otvet.send_keys(y)

checkbox = driver.find_element_by_css_selector('#robotCheckbox')
checkbox.click()
radio_btn = driver.find_element_by_css_selector('#robotsRule')
radio_btn.click()
btn = driver.find_element_by_css_selector('button[type="submit"]')
btn.click()
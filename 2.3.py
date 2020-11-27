from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

driver = webdriver.Chrome(executable_path='chromedriver.exe')
driver.implicitly_wait(5)
driver.get('http://suninjuly.github.io/redirect_accept.html')

btn = driver.find_element_by_css_selector('button[type="submit"]')
btn.click()

new_window = driver.window_handles[1]
driver.switch_to.window(new_window)

#alert = driver.switch_to.alert
#alert.accept()

x_element = driver.find_element_by_id("input_value")
x_element = x_element.text
x = x_element
y = calc(x)

otvet = driver.find_element_by_css_selector('#answer')
otvet.send_keys(y)

btn2 = driver.find_element_by_css_selector('button[type="submit"]')
btn2.click()
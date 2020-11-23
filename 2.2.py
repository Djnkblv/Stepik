from idlelib import browser
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select


driver = webdriver.Chrome(executable_path='chromedriver.exe')
driver.implicitly_wait(5)
driver.get('http://suninjuly.github.io/selects1.html')

x_select = driver.find_element_by_css_selector('#num1')
int(x) = x_select.text
y_select = driver.find_element_by_css_selector('#num2')
int(y) = y_select.text
int(otvet) = x + y


select = Select(browser.find_element_by_tag_name("select"))
select.select_by_value(otvet)
select.click()
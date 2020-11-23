from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import secret

driver = webdriver.Chrome(executable_path='chromedriver.exe')
driver.implicitly_wait(5)
driver.get('https://dispace.edu.nstu.ru')

btn = driver.find_element_by_css_selector('div.input-field>a')
btn.click()

login = driver.find_element_by_css_selector('input[name="callback_0"]')
password = driver.find_element_by_css_selector('input[name="callback_1"]')
submit = driver.find_element_by_css_selector('input[name="callback_2"]')
login.send_keys(secret.login)
password.send_keys(secret.password)
submit.click()

menu = driver.find_element_by_css_selector('a[data-target="dropdown-submenu-6"]')
menu.click()
menu_shedule = driver.find_element_by_css_selector('ul#dropdown-submenu-6>li:nth-child(3)>a')
menu_shedule.click()

webinar_title = driver.find_element_by_css_selector('a[event_id="34723"]')
mo = ActionChains(driver).move_to_element(webinar_title)
mo.perform()
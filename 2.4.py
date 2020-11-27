from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

browser = webdriver.Chrome()
browser.implicitly_wait(5)
browser.get("http://suninjuly.github.io/explicit_wait2.html")

button = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100")
    )
button = browser.find_element_by_css_selector('#book')
button.click()
#message = browser.find_element_by_id("verify_message")

x_element = browser.find_element_by_id("input_value")
x_element = x_element.text
x = x_element
y = calc(x)

otvet = browser.find_element_by_css_selector('#answer')
otvet.send_keys(y)

btn2 = browser.find_element_by_css_selector('button[type="submit"]')
btn2.click()


#assert "successful" in message.text
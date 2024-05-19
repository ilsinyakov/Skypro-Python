from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()

driver.get('http://uitestingplayground.com/textinput')

button_name_field = driver.find_element(By.ID, 'newButtonName')
button_name_field.send_keys('SkyPro')

button = driver.find_element(By.ID, 'updatingButton')
button.click()

txt = button.text
print(txt)

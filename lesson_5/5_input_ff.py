from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()

driver.get('http://the-internet.herokuapp.com/inputs')

field = driver.find_element(By.TAG_NAME, 'input')
field.send_keys('1000')
field.clear()
field.send_keys('999')

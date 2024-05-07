from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()

driver.get('http://the-internet.herokuapp.com/add_remove_elements/')

add_element_button = driver.find_element(By.TAG_NAME, 'button')
for i in range(5):
    add_element_button.click()

delete_buttons = driver.find_elements(By.CLASS_NAME, 'added-manually')
print(len(delete_buttons))

from selenium import webdriver
from selenium.webdriver.common.by import By


for i in range(3):
    driver = webdriver.Chrome()
    driver.get('http://uitestingplayground.com/dynamicid')

    blue_button = driver.find_element(By.CLASS_NAME, 'btn')
    blue_button.click()

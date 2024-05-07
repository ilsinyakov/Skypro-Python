from selenium import webdriver
from selenium.webdriver.common.by import By


for i in range(3):
    driver = webdriver.Chrome()

    driver.get('http://uitestingplayground.com/classattr')

    blue_buttons = driver.find_element(By.CLASS_NAME, 'btn-primary')
    blue_buttons.click()

from selenium import webdriver
from selenium.webdriver.common.by import By

from time import sleep


for i in range(3):
    driver = webdriver.Firefox()

    driver.get('http://uitestingplayground.com/classattr')

    blue_buttons = driver.find_element(By.CLASS_NAME, 'btn-primary')
    blue_buttons.click()
    sleep(3)

    driver.quit()

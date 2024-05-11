from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


driver = webdriver.Chrome()

driver.get('http://uitestingplayground.com/ajax')

ajax_button = driver.find_element(By.ID, 'ajaxButton')
ajax_button.click()

data_element = WebDriverWait(driver, 40).until(
    ec.presence_of_element_located((By.CLASS_NAME, 'bg-success'))
)
txt = data_element.text
print(txt)

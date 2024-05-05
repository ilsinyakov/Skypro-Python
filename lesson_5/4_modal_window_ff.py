from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


driver = webdriver.Firefox()

driver.get('http://the-internet.herokuapp.com/entry_ad')

close_button = WebDriverWait(driver, 5).until(ec.element_to_be_clickable((By.CSS_SELECTOR, '.modal-footer p')))
close_button.click()

driver.quit()

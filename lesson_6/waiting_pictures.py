from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


driver = webdriver.Chrome()

driver.get(' https://bonigarcia.dev/selenium-webdriver-java/loading-images.html')

WebDriverWait(driver, 40).until(
    ec.presence_of_element_located((By.ID, 'landscape'))
)
images = driver.find_elements(By.CSS_SELECTOR, '#image-container img')
src_3 = images[2].get_attribute('src')
print(src_3)

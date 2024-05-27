from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


driver = webdriver.Chrome()
driver.get('https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html')


def test_calculator():
    delay_field = driver.find_element(By.ID, 'delay')
    delay_field.clear()
    delay_field.send_keys('45')

    button_7 = driver.find_element(By.XPATH, '//*[contains(text(),"7")]')
    button_7.click()

    button_plus = driver.find_element(By.XPATH, '//*[contains(text(),"+")]')
    button_plus.click()

    button_8 = driver.find_element(By.XPATH, '//*[contains(text(),"8")]')
    button_8.click()

    button_equal = driver.find_element(By.XPATH, '//*[contains(text(),"=")]')
    button_equal.click()

    # increased wait from 45 to 47
    (WebDriverWait(driver, 47).
     until(ec.text_to_be_present_in_element((By.CLASS_NAME, 'screen'), '15')))

    assert driver.find_element(By.CLASS_NAME, 'screen').text == '15', \
        'Result is not 15'

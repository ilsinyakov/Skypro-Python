from selenium import webdriver
from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as ec


driver = webdriver.Chrome()
driver.get('https://www.saucedemo.com/')


def test_shop():
    user_name_field = driver.find_element(By.ID, 'user-name')
    user_name_field.send_keys('standard_user')

    password_field = driver.find_element(By.ID, 'password')
    password_field.send_keys('secret_sauce')

    login_button = driver.find_element(By.ID, 'login-button')
    login_button.click()

    backpack_button = driver.find_element(By.ID, 'add-to-cart-sauce-labs-backpack')
    backpack_button.click()

    t_short_button = driver.find_element(By.ID, 'add-to-cart-sauce-labs-bolt-t-shirt')
    t_short_button.click()

    onesie_button = driver.find_element(By.ID, 'add-to-cart-sauce-labs-onesie')
    onesie_button.click()

    cart_link = driver.find_element(By.CSS_SELECTOR, '[data-test="shopping-cart-link"]')
    cart_link.click()

    checkout_button = driver.find_element(By.ID, 'checkout')
    checkout_button.click()

    first_name_field = driver.find_element(By.ID, 'first-name')
    first_name_field.send_keys('Ilya')

    last_name_field = driver.find_element(By.ID, 'last-name')
    last_name_field.send_keys('Sinyakov')

    postal_code_field = driver.find_element(By.ID, 'postal-code')
    postal_code_field.send_keys('123456')

    continue_button = driver.find_element(By.ID, 'continue')
    continue_button.click()

    total_element = driver.find_element(By.CSS_SELECTOR, '[data-test="total-label"]')
    total = total_element.text

    assert total[-6:] == '$58.29', 'Total is not correct'

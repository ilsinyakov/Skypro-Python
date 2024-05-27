from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.get('https://bonigarcia.dev/selenium-webdriver-java/data-types.html')


def test_fill_form():
    first_name_field = driver.find_element(By.NAME, 'first-name')
    first_name_field.send_keys('Иван')

    last_name_field = driver.find_element(By.NAME, 'last-name')
    last_name_field.send_keys('Петров')

    address_field = driver.find_element(By.NAME, 'address')
    address_field.send_keys('Ленина, 55-3')

    email_field = driver.find_element(By.NAME, 'e-mail')
    email_field.send_keys('test@skypro.com')

    phone_field = driver.find_element(By.NAME, 'phone')
    phone_field.send_keys('+7985899998787')

    city_field = driver.find_element(By.NAME, 'city')
    city_field.send_keys('Москва')

    country_field = driver.find_element(By.NAME, 'country')
    country_field.send_keys('Россия')

    job_field = driver.find_element(By.NAME, 'job-position')
    job_field.send_keys('QA')

    company_field = driver.find_element(By.NAME, 'company')
    company_field.send_keys('SkyPro')

    submit_button = driver.find_element(By.CSS_SELECTOR, '[type="submit"]')
    submit_button.click()

    fields = driver.find_elements(By.XPATH, '//*[@id]')

    for field in fields:
        if field.get_attribute('id') != 'zip-code':
            assert field.value_of_css_property('background-color') == 'rgba(209, 231, 221, 1)', \
                   f'Field {field.get_attribute("id")} is not green'
        else:
            assert field.value_of_css_property('background-color') == 'rgba(248, 215, 218, 1)', \
                   f'Field zip-code is not red'

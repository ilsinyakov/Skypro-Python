from selenium.webdriver.common.by import By


class MainPageForm:
    def __init__(self, browser):
        self.browser = browser
        self.browser.get('https://bonigarcia.dev/selenium-webdriver-java/data-types.html')

    def fill_form(self):
        first_name_field = self.browser.find_element(By.NAME, 'first-name')
        first_name_field.send_keys('Иван')

        last_name_field = self.browser.find_element(By.NAME, 'last-name')
        last_name_field.send_keys('Петров')

        address_field = self.browser.find_element(By.NAME, 'address')
        address_field.send_keys('Ленина, 55-3')

        email_field = self.browser.find_element(By.NAME, 'e-mail')
        email_field.send_keys('test@skypro.com')

        # phone_field = self.browser.find_element(By.NAME, 'phone')
        # phone_field.send_keys('+7985899998787')

        city_field = self.browser.find_element(By.NAME, 'city')
        city_field.send_keys('Москва')

        country_field = self.browser.find_element(By.NAME, 'country')
        country_field.send_keys('Россия')

        job_field = self.browser.find_element(By.NAME, 'job-position')
        job_field.send_keys('QA')

        company_field = self.browser.find_element(By.NAME, 'company')
        company_field.send_keys('SkyPro')

        submit_button = self.browser.find_element(By.CSS_SELECTOR, '[type="submit"]')
        submit_button.click()

    def is_zip_code_red(self):
        zip_field = self.browser.find_element(By.ID, 'zip-code')
        if zip_field.value_of_css_property('background-color') == 'rgba(248, 215, 218, 1)':
            return True
        else:
            return False

    def is_fields_green(self):
        is_true = False
        fields = self.browser.find_elements(By.XPATH, '//*[@id and not (@id="zip-code")]')
        for field in fields:            
            if field.value_of_css_property('background-color') == 'rgba(209, 231, 221, 1)':
                is_true = True
            else:
                is_true = False
                return is_true
        return is_true

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class MainPageCalculator:
    def __init__(self, browser) -> None:
        self.browser = browser
        self.browser.get('https://bonigarcia.dev/selenium-webdriver-java/'
                         'slow-calculator.html')

    def click_button(self, sym: str) -> None:
        '''
        Click button
        '''
        button = self.browser.find_element(By.XPATH,
                                           f'//*[contains(text(),"{sym}")]')
        button.click()

    def get_result(self) -> str:
        '''
        Get calculated result
        '''
        # increased wait from 45 to 47
        WebDriverWait(self.browser, 47).until(
            ec.text_to_be_present_in_element((By.CLASS_NAME, 'screen'), '15')
            )
        return self.browser.find_element(By.CLASS_NAME, 'screen').text

    def set_delay(self, delay: str) -> None:
        '''
        Set delay
        '''
        delay_field = self.browser.find_element(By.ID, 'delay')
        delay_field.clear()
        delay_field.send_keys(delay)

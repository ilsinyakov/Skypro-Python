from selenium.webdriver.common.by import By


class Checkout1Page:
    def __init__(self, browser) -> None:
        self.browser = browser

    def fill_form(self, first_name: str, last_name: str,
                  postal_code: str) -> None:
        '''
        Fill form
        '''
        first_name_field = self.browser.find_element(By.ID, 'first-name')
        first_name_field.send_keys(first_name)

        last_name_field = self.browser.find_element(By.ID, 'last-name')
        last_name_field.send_keys(last_name)

        postal_code_field = self.browser.find_element(By.ID, 'postal-code')
        postal_code_field.send_keys(postal_code)

    def click_continue(self) -> None:
        '''
        Click continue button
        '''
        continue_button = self.browser.find_element(By.ID, 'continue')
        continue_button.click()

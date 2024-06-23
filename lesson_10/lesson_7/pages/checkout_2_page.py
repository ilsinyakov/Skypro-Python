from selenium.webdriver.common.by import By


class Checkout2Page:
    def __init__(self, browser) -> None:
        self.browser = browser

    def get_total(self) -> str:
        '''
        Get total
        '''
        total_element = self.browser.find_element(By.CSS_SELECTOR,
                                                  '[data-test="total-label"]')
        total = total_element.text
        return total[-6:]

from selenium.webdriver.common.by import By


class CartPage:
    def __init__(self, browser) -> None:
        self.browser = browser

    def checkout(self) -> None:
        '''
        Go to checkout
        '''
        checkout_button = self.browser.find_element(By.ID, 'checkout')
        checkout_button.click()

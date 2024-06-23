from selenium.webdriver.common.by import By


class MainPageShop:
    def __init__(self, browser) -> None:
        self.browser = browser
        self.browser.get('https://www.saucedemo.com/')

    def login(self, user_name: str, password: str) -> None:
        '''
        Log-in User
        '''
        user_name_field = self.browser.find_element(By.ID, 'user-name')
        user_name_field.send_keys(user_name)

        password_field = self.browser.find_element(By.ID, 'password')
        password_field.send_keys(password)

        login_button = self.browser.find_element(By.ID, 'login-button')
        login_button.click()

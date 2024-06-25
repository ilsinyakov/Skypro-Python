import allure
from selenium import webdriver
from pages.MainPageCalculator import MainPageCalculator


def test_calculator():
    browser = webdriver.Chrome()
    main_page = MainPageCalculator(browser)

    with allure.step('Make calculations'):
        main_page.set_delay('45')
        main_page.click_button('7')
        main_page.click_button('+')
        main_page.click_button('8')
        main_page.click_button('=')

    with allure.step('Get result'):
        result = main_page.get_result()

    with allure.step('Check that result is correct'):
        assert result == '15', 'Result is not 15'

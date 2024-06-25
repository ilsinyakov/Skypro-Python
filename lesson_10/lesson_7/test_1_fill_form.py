import allure
from selenium import webdriver
from pages.MainPageForm import MainPageForm


def test_fill_form():
    browser = webdriver.Chrome()
    with allure.step('Fill form'):
        main_page = MainPageForm(browser)
        main_page.fill_form()

    with allure.step('Check that zip code is red'):
        assert main_page.is_zip_code_red(), 'Field zip-code is not red'

    with allure.step('Check that other fields is green'):
        assert main_page.is_fields_green(), 'Field is not green'

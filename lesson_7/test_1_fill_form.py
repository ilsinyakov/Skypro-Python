from selenium import webdriver
from pages.main_page_form import MainPageForm


def test_fill_form():
    browser = webdriver.Chrome()
    main_page = MainPageForm(browser)    
    main_page.fill_form()    
    assert main_page.is_zip_code_red(), 'Field zip-code is not red'
    assert main_page.is_fields_green(), 'Field is not green'

from selenium import webdriver
from pages.main_page_calculator import MainPageCalculator
from time import sleep


def test_calculator():
    browser = webdriver.Chrome()
    main_page = MainPageCalculator(browser)

    main_page.set_delay('45')
    main_page.click_button('7')    
    main_page.click_button('+')    
    main_page.click_button('8')    
    main_page.click_button('=')    
    result = main_page.get_result()
    assert result == '15', 'Result is not 15'

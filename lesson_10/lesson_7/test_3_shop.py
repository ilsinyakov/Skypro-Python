import allure
from selenium import webdriver
from pages.MainPageShop import MainPageShop
from pages.CatalogPage import CatalogPage
from pages.CartPage import CartPage
from pages.Checkout1Page import Checkout1Page
from pages.Checkout2Page import Checkout2Page


def test_shop():
    browser = webdriver.Chrome()

    with allure.step('Log in an existing user'):
        main_page = MainPageShop(browser)
        main_page.login('standard_user', 'secret_sauce')

    with allure.step('Add product to the cart'):
        catalog_page = CatalogPage(browser)
        catalog_page.add_product_to_cart()

    with allure.step('Go to the cart page'):
        catalog_page.go_to_cart()

    with allure.step('Checkout'):
        cart_page = CartPage(browser)
        cart_page.checkout()

    with allure.step('Fill order form'):
        checkout_1_page = Checkout1Page(browser)
        checkout_1_page.fill_form('Ilya', 'Sinyakov', '123456')
    with allure.step('Click continue'):
        checkout_1_page.click_continue()

    with allure.step('Get total'):
        checkout_2_page = Checkout2Page(browser)
        total = checkout_2_page.get_total()

    browser.quit()

    with allure.step('Check that the total is correct'):
        assert total == '$58.29', 'Total is not correct'

from steam_online_store_UI.pages.main_page import main_page
from steam_online_store_UI.pages.search_page import search_page
from steam_online_store_UI.pages.cart_page import cart_page

import allure
from allure_commons.types import Severity


@allure.tag('web')
@allure.severity(Severity.CRITICAL)
@allure.feature('Cart')
@allure.story('Add game to cart')
@allure.label('owner', 'Roman Tropin')
def test_add_game_to_cart():
    main_page.open_main_page()
    search_page.find_game('ICARUS')
    search_page.click_on_first_game_in_search_row('ICARUS')
    cart_page.add_game_to_cart()
    cart_page.move_to_cart()

    cart_page.check_game_in_cart('Icarus')


@allure.tag('web')
@allure.severity(Severity.CRITICAL)
@allure.feature('Cart')
@allure.story('Clear cart')
@allure.label('owner', 'Roman Tropin')
def test_clear_cart():
    main_page.open_main_page()
    search_page.find_game('ICARUS')
    search_page.click_on_first_game_in_search_row('ICARUS')
    cart_page.add_game_to_cart()
    cart_page.move_to_cart()
    cart_page.clear_cart()

    cart_page.check_empty_cart()

from steam_online_store_UI.pages.main_page import main_page
from steam_online_store_UI.pages.search_page import search_page

import allure
from allure_commons.types import Severity


@allure.tag('web')
@allure.severity(Severity.MINOR)
@allure.feature('Search')
@allure.story('Appear game in dropdown list')
@allure.label('owner', 'Roman Tropin')
def test_game_appears_in_the_dropdown_list():
    main_page.open_main_page()
    search_page.type_game_name_in_search_field('Spider-man')

    search_page.should_game_appear_in_dropdown_list("Marvel's Spider-Man 2")


@allure.tag('web')
@allure.severity(Severity.BLOCKER)
@allure.feature('Search')
@allure.story('Find the game in search result')
@allure.label('owner', 'Roman Tropin')
def test_successful_search_game():
    main_page.open_main_page()
    search_page.find_game('Spider-man')

    search_page.should_game_appear_in_search_result("Marvel's Spider-Man 2")


@allure.tag('web')
@allure.severity(Severity.MINOR)
@allure.feature('Search')
@allure.story('Entering incorrect data into the search, no games should be found')
@allure.label('owner', 'Roman Tropin')
def test_not_successful_search_game():
    main_page.open_main_page()
    search_page.find_game('beliberda')

    search_page.should_find_zero_game_in_not_successful_search()

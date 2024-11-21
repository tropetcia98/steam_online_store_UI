from steam_online_store_UI.pages.main_page import main_page

import allure
from allure_commons.types import Severity


@allure.tag('web')
@allure.severity(Severity.BLOCKER)
@allure.feature('Language')
@allure.story('Switch language')
@allure.label('owner', 'Roman Tropin')
def test_for_changing_language():
    main_page.open_main_page()
    main_page.click_on_language_button()
    main_page.choose_language('english')

    main_page.should_change_language_the_language_selection_button(language_button='language')
    main_page.should_change_language_the_install_steam_button(install_steam_button='Install Steam')

from steam_online_store_UI.pages.main_page import main_page
from steam_online_store_UI.pages.authorisation_page import authorisation_page

import allure
from allure_commons.types import Severity


@allure.tag('web')
@allure.severity(Severity.CRITICAL)
@allure.feature('Unsuccessful authorization')
@allure.story('Failed authorization attempt')
@allure.label('owner', 'Roman Tropin')
def test_not_successful_authorisation():
    main_page.open_main_page()
    main_page.click_on_login_button()
    authorisation_page.type_account_name('Error')
    authorisation_page.type_password('Bad')
    authorisation_page.click_on_sign_in_button()
    authorisation_page.should_authorization_error_text_appear()

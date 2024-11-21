from selene import browser, have
import allure


class MainPage:

    def __init__(self):
        self.login_button = browser.all('.global_action_link').element_by(have.text('login'))
        self.language_button = browser.element('#language_pulldown')

    def open_main_page(self):
        with allure.step('Открыть главную страницу "Steam".'):
            browser.open('/')

    def click_on_login_button(self):
        with allure.step('Кликнуть на кнопку логина для открытия страницы авторизации'):
            self.login_button.click()

    def click_on_language_button(self):
        with allure.step('Кликнуть на кнопку выбора языка.'):
            self.language_button.click()

    def choose_language(self, language):
        with allure.step(f"Выбрать {language} язык."):
            browser.element(f'[href="?l={language}"]').click()

    def should_change_language_the_language_selection_button(self, language_button):
        with allure.step(f'Проверяем, что кнопка "Язык" сменила свой язык на {language_button}.'):
            browser.element('#language_pulldown').should(have.text(language_button))

    def should_change_language_the_install_steam_button(self, install_steam_button):
        with allure.step(f'Проверяем, что кнопка "Установить Steam" сменила свой язык на {install_steam_button} .'):
            browser.element('.header_installsteam_btn_content').should(have.text(install_steam_button))


main_page = MainPage()

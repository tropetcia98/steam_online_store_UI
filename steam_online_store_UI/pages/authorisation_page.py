import allure
from selene import browser, have


class AuthorisationPage:

    def __init__(self):
        self.name = browser.element('[type="text"]')
        self.password = browser.element('[type="password"]')
        self.sign_in_button = browser.element('[type="submit"]')

    def type_account_name(self, value):
        with allure.step('Ввести имя пользователя.'):
            self.name.type(value)

    def type_password(self, value):
        with allure.step('Ввести пароль.'):
            self.password.type(value)

    def click_on_sign_in_button(self):
        with allure.step('Нажать на кнопку "Войти" для входа в аккаунт.'):
            self.sign_in_button.click()

    def should_authorization_error_text_appear(self):
        with allure.step('Должен появиться текст ошибки авторизации'):
            browser.element('._1W_6HXiG4JJ0By1qN_0fGZ').should(
                have.text('Please check your password and account name and try again.'))


authorisation_page = AuthorisationPage()

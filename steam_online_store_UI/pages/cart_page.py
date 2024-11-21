import allure
from selene import browser, have


class CartPage:

    def __init__(self):
        self.add_to_cart_button = browser.element('.btn_addtocart')
        self.move_to_cart_button = browser.all('[type="button"]').element_by(have.text('View My Cart'))
        self.clear_cart_button = browser.element('._12zYFuKO2U-1QfeVxlGfwF')

    def add_game_to_cart(self):
        with allure.step('Добавить игру в корзину.'):
            self.add_to_cart_button.click()

    def move_to_cart(self):
        with allure.step('Перейти в корзину.'):
            self.move_to_cart_button.click()

    def clear_cart(self):
        with allure.step('Очистить корзину.'):
            self.clear_cart_button.click()

    def check_game_in_cart(self, game_name):
        with allure.step(f'Проверяем наличие игры {game_name} в корзине.'):
            browser.element('.EflKs0JjldhDSxbUBaiOp').should(have.text(game_name))

    def check_empty_cart(self):
        with allure.step('Проверяем что корзина пустая.'):
            browser.element('.EflKs0JjldhDSxbUBaiOp').should(have.text('Your cart is empty.'))


cart_page = CartPage()

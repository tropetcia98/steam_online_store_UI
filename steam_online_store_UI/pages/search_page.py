from selene import browser, by, have
import allure


class SearchPage:

    def __init__(self):
        self.find_game_field = browser.element('#store_nav_search_term')

    def find_game(self, game_name):
        with allure.step(f'Ввести в поле поиска название игры: {game_name} и искать её.'):
            self.find_game_field.type(game_name).press_enter()

    def type_game_name_in_search_field(self, game_name):
        with allure.step(f'Ввести в поле поиска название игры: {game_name}.'):
            self.find_game_field.type('Spider-man')

    def click_on_first_game_in_search_row(self, game_name):
        with allure.step(f'Кликнуть на первую игру: "{game_name}" в результате поиска.'):
            browser.all(by.text(game_name)).first.click()

    def should_game_appear_in_dropdown_list(self, game_name):
        with allure.step(f'Игра "{game_name}" должна появиться в выпадающем списке.'):
            browser.element('#search_suggestion_contents').should(have.text(game_name))

    def should_game_appear_in_search_result(self, game_name):
        with allure.step(f'Проверяем что игра {game_name} была найдена в результате поиска'):
            browser.element('#search_result_container').should(have.text(game_name))

    def should_find_zero_game_in_not_successful_search(self):
        with allure.step(f'Проверяем, что не было найдено ни одной игры'):
            browser.element('.search_results_count').should(have.text('0 results match your search.'))


search_page = SearchPage()

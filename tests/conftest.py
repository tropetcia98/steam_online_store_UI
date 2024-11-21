import pytest

from selene import browser

from steam_online_store_UI.utils import attach


@pytest.fixture(scope='function', autouse=True)
def setup_browser():
    browser.config.base_url = 'https://store.steampowered.com'
    browser.config.window_height = 1080
    browser.config.window_width = 1920

    yield browser

    attach.add_screenshot(browser)
    attach.add_logs(browser)
    attach.add_html(browser)

    browser.quit()

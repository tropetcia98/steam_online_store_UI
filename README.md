# Проект по автоматизации тестирования Steam

## Стек технологий 
<p align="left">
<img align="center" src="steam_online_store_UI/images/python-original-wordmark.svg" width="40" height="40" alt="Python"/>
<img align="center" src="steam_online_store_UI/images/AllureReport.png" width="40" height="40" alt="Python"/>
<img align="center" src="steam_online_store_UI/images/AllureTestOps.png" width="40" height="40" alt="Python"/>
<img align="center" src="steam_online_store_UI/images/Selene.png" width="40" height="40" alt="Python"/>
<img align="center" src="steam_online_store_UI/images/Telegram.png" width="40" height="40" alt="Python"/>
<img align="center" src="steam_online_store_UI/images/jenkins-original.svg" width="40" height="40" alt="Python"/>
<img align="center" src="steam_online_store_UI/images/pycharm-original.svg" width="40" height="40" alt="Python"/>
<img align="center" src="steam_online_store_UI/images/pytest-original-wordmark.svg" width="40" height="40" alt="Python"/>
<img align="center" src="steam_online_store_UI/images/selenium-original.svg" width="40" height="40" alt="Python"/>
<img align="center" src="steam_online_store_UI/images/selenoid.png" width="40" height="40" alt="Python"/>

В данном проекте автотесты написаны на <code>Python</code> с использованием <code>Selenium</code>, <code>Selene</code> и <code>Pytest</code> для UI-тестов
>
> <code>Selenoid</code> выполняет запуск браузеров в контейнерах <code>Docker</code>.
>
> <code>Allure Report</code> формирует отчет о запуске тестов.
>
> <code>Jenkins</code> выполняет запуск тестов.
> После завершения прогона отправляются уведомления с помощью бота в <code>Telegram</code>.

## Список реализуемых проверок:
- Проверка добавления товара в корзину
- Проверка очищения корзины
- Проверка на смену языка сайта
- Проверка отображения товара в выпадающем списке при его поиске
- Проверка поиска товара
- Проверка появления ошибки при поиске некорректного товара
- Проверка появления ошибки при авторизации с ошибочными данными

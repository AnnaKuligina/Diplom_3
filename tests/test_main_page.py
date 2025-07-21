import allure
from pages.main_page import MainPage
from pages.account_page import AccountPage
from data import EMAIL, PASSWORD


@allure.feature('Основная функциональноcть')
@allure.story('Тесты функционала главной страницы')
class TestMainPage:

    @allure.title('Переход в конструктор по клику')
    def test_constructor_navigation(self, driver):
        main_page = MainPage(driver)
        account_page = AccountPage(driver)

        with allure.step('Открытие страницы входа'):
            account_page.open_login_page()

        with allure.step('Нажимаем на "Конструктор"'):
            main_page.click_constructor()

        with allure.step('Проверка того, что секция конструктора отображается'):
            assert main_page.is_constructor_visible(), "Секция конструктора не отображается!"

    @allure.title('Переход в ленту заказов по клику')
    def test_order_feed_navigation(self, driver):
        main_page = MainPage(driver)
        account_page = AccountPage(driver)

        with allure.step('Открытие страницы входа'):
            account_page.open_login_page()

        with allure.step('Нажатие на "Лента заказов"'):
            main_page.click_order_feed()

        with allure.step('Проверка того, что счетчик выполненных заказов отображается'):
            assert main_page.is_order_feed_counter_visible(), "Счетчик выполненных заказов не отображается!"

    @allure.title('Отображение деталей ингредиента')
    def test_ingredient_details_display(self, driver):
        main_page = MainPage(driver)
        account_page = AccountPage(driver)

        with allure.step('Открытие страницы входа'):
            account_page.open_login_page()

        with allure.step('Нажатие на "Конструктор"'):
            main_page.click_constructor()

        with allure.step('Нажатие на ингредиент'):
            main_page.click_ingredient()

        with allure.step('Проверка того, что окно с деталями ингредиента отображается'):
            assert main_page.are_ingredient_details_visible(), "Детали ингредиента не отображаются!"

    @allure.title('Закрытие окна деталей ингредиента')
    def test_ingredient_details_close(self, driver):
        main_page = MainPage(driver)
        account_page = AccountPage(driver)

        with allure.step('Открытие страницы входа'):
            account_page.open_login_page()

        with allure.step('Нажатие на "Конструктор"'):
            main_page.click_constructor()

        with allure.step('Нажатие на ингредиент'):
            main_page.click_ingredient()

        with allure.step('Закрытие окна с деталями ингредиента'):
            main_page.close_ingredient_details()

        with allure.step('Проверка того, что окно с деталями ингредиента закрыто'):
            assert not main_page.are_ingredient_details_visible()

    @allure.title('Увеличение счетчика ингредиентов')
    def test_ingredient_counter_increment(self, driver):
        main_page = MainPage(driver)
        account_page = AccountPage(driver)

        with allure.step('Открытие страницы входа'):
            account_page.open_login_page()

        with allure.step('Нажатие на "Конструктор"'):
            main_page.click_constructor()

        with allure.step('Получение начального значения счетчика ингредиентов'):
            initial_counter = main_page.get_ingredient_counter()

        with allure.step('Добавление ингредиента в заказ'):
            main_page.drag_and_drop_ingredient()

        with allure.step('Проверка того, что счетчик увеличился'):
            updated_counter = main_page.get_ingredient_counter()

        assert updated_counter == initial_counter + 2, \
            f"Счетчик не увеличился! Ожидалось: {initial_counter + 2}, но получено: {updated_counter}"
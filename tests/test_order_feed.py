import allure
from pages.order_feed_page import OrderFeedPage
from pages.main_page import MainPage
from pages.account_page import AccountPage
from data import EMAIL, PASSWORD

@allure.feature('Лента заказов')
@allure.story('Тесты раздела "Лента заказов')
class TestOrderPage:

    @allure.title('Открытие всплывающего окна с деталями заказа')
    def test_order_modal_opens(self, driver):
        order_feed_page = OrderFeedPage(driver)

        with allure.step('Открытие ленты заказов'):
            order_feed_page.open_feed_page()

        with allure.step('Клик по последнему заказу'):
            order_feed_page.click_last_order()

        with allure.step('Проверяем отображение всплывающего окна'):
            content = order_feed_page.get_order_details_content()
            assert content != "", "Всплывающее окно с деталями заказа не открылось"

    @allure.title('Отображение созданного заказа в ленте заказов')
    def test_new_order_appears_in_feed(self, driver):
        order_feed_page = OrderFeedPage(driver)
        main_page = MainPage(driver)
        account_page = AccountPage(driver)

        with allure.step('Выполняем вход в аккаунт'):
            account_page.login(EMAIL, PASSWORD)

        with allure.step('Создаем новый заказ'):
            main_page.drag_and_drop_ingredient()
            order_feed_page.place_order()

        with allure.step('Получаем идентификатор заказа'):
            order_id = order_feed_page.get_order_id()

        with allure.step('Закрываем детали заказа и открываем ленту заказов'):
            order_feed_page.close_order_details()
            order_feed_page.open_feed_page()

        with allure.step('Проверяем, что заказ отображается в ленте заказов'):
            assert order_feed_page.is_order_in_feed(order_id), \
                f"Идентификатор заказа {order_id} не найден в ленте заказов"

    @allure.title('Увеличение общего счетчика заказов после создания нового')
    def test_total_orders_counter_increment(self, driver):
        order_feed_page = OrderFeedPage(driver)
        main_page = MainPage(driver)
        account_page = AccountPage(driver)

        with allure.step('Вход в аккаунт'):
            account_page.login(EMAIL, PASSWORD)

        with allure.step('Открытие ленты заказов'):
            order_feed_page.click_feed()

        with allure.step('Получаем начальный счётчик заказов'):
            initial_total_orders = order_feed_page.get_total_orders_count()

        with allure.step('Создаем новый заказ'):
            order_feed_page.click_constructor()
            main_page.drag_and_drop_ingredient()
            order_feed_page.place_order()
            order_feed_page.get_order_id()
            order_feed_page.close_order_details()

        with allure.step('Проверяем, что общий счётчик заказов увеличился'):
            order_feed_page.open_feed_page()
            updated_total_orders = order_feed_page.get_total_orders_count()
            assert updated_total_orders > initial_total_orders, \
                f"Ожидалось увеличение счетчика. Было: {initial_total_orders}, стало: {updated_total_orders}"

    @allure.title('Увеличение дневного счетчика заказов после создания нового')
    def test_today_orders_counter_increment(self, driver):
        order_feed_page = OrderFeedPage(driver)
        main_page = MainPage(driver)
        account_page = AccountPage(driver)

        with allure.step('Вход в аккаунт'):
            account_page.login(EMAIL, PASSWORD)

        with allure.step('Открытие ленты заказов'):
            order_feed_page.click_feed()

        with allure.step('Получаем начальный счётчик заказов за сегодня'):
            initial_today_orders = order_feed_page.get_today_orders_count()
            order_feed_page.click_constructor()

        with allure.step('Создаем новый заказ'):
            order_feed_page.click_constructor()
            main_page.drag_and_drop_ingredient()
            order_feed_page.place_order()
            order_feed_page.get_order_id()

        with allure.step('Закрываем детали заказа и открываем ленту заказов'):
            order_feed_page.close_order_details()
            order_feed_page.click_feed()

        with allure.step('Проверяем, что счётчик заказов за сегодня увеличился'):
            updated_today_orders = order_feed_page.get_today_orders_count()
            assert updated_today_orders > initial_today_orders, \
                f"Ожидалось увеличение счетчика на 1. Было: {initial_today_orders}, стало: {updated_today_orders}"

    @allure.title('Появление номера заказа в разделе "В работе"')
    def test_order_appears_in_progress_section(self, driver):
        order_feed_page = OrderFeedPage(driver)
        main_page = MainPage(driver)
        account_page = AccountPage(driver)

        with allure.step('Вход в аккаунт'):
            account_page.login(EMAIL, PASSWORD)

        with allure.step('Создание нового заказа'):
            order_feed_page.click_constructor()
            main_page.drag_and_drop_ingredient()
            order_feed_page.place_order()

        with allure.step('Получение идентификатора заказа'):
            order_id = order_feed_page.get_order_id()

        with allure.step('Закрытие всплывающего окна, проверка раздела "В работе"'):
            order_feed_page.close_order_details()
            order_feed_page.click_feed()

        with allure.step('Проверка появления номера заказа в разделе "В работе"'):
            assert order_feed_page.is_order_in_progress(order_id), \
                f"Номер заказа {order_id} не появился в разделе 'В работе'"
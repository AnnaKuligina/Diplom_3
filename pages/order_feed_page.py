import allure
from pages.base_page import BasePage
from locators.order_feed_locators import OrderFeedLocators
from curl import FEED_URL


class OrderFeedPage(BasePage):
    @allure.step("Кликнуть на последний заказ в ленте")
    def click_last_order(self):
        self.click_on_element(OrderFeedLocators.RECENT_ORDER_CARD)

    @allure.step("Получить состав заказа из деталей")
    def get_order_details_content(self):
        return self.get_text(OrderFeedLocators.ORDER_COMPOSITION_TEXT)

    @allure.step("Получить общее количество заказов за все время")
    def get_total_orders_count(self):
        return int(self.get_text(OrderFeedLocators.ALL_TIME_ORDERS_COUNT))

    @allure.step("Получить количество заказов за сегодня")
    def get_today_orders_count(self):
        element = self.find_element_with_wait(OrderFeedLocators.TODAY_ORDERS_COUNT)
        return int(element.text.strip())

    @allure.step("Открыть страницу ленты заказов")
    def open_feed_page(self):
        self.open_url(FEED_URL)
        self.wait_until_visible(OrderFeedLocators.FEED_HEADER)

    @allure.step("Перейти в конструктор из ленты заказов")
    def click_constructor(self):
        self.click_on_element(OrderFeedLocators.CONSTRUCTOR_LINK)

    @allure.step("Перейти в ленту заказов")
    def click_feed(self):
        self.click_when_ready(OrderFeedLocators.FEED_LINK)
        self.wait_until_visible(OrderFeedLocators.FEED_HEADER)

    @allure.step("Получить статус заказа")
    def get_order_status(self):
        element = self.find_element_with_wait(OrderFeedLocators.ORDER_STATUS_TEXT)
        return element.text.strip()

    @allure.step("Оформить заказ")
    def place_order(self):
        self.click_on_element(OrderFeedLocators.MAKE_ORDER_BUTTON)

    @allure.step("Кликнуть на кнопку 'Личный кабинет'")
    def click_account_button(self):
        self.click_when_ready(OrderFeedLocators.PROFILE_LINK)

    @allure.step("Открыть историю заказов")
    def click_order_history(self):
        self.click_on_element(OrderFeedLocators.ORDER_HISTORY_LINK)

    @allure.step("Закрыть детали заказа")
    def close_order_details(self):
        try:
            return self.safe_close_modal(
                close_button_locator=OrderFeedLocators.CLOSE_DETAILS_BUTTON,
                overlay_locator=OrderFeedLocators.LOADING_OVERLAY,
                timeout=20
            )
        except Exception as e:
            print(f"Ошибка при закрытии деталей заказа: {str(e)}")
            raise

    @allure.step("Получить номер заказа")
    def get_order_id(self):
        initial_text = self.get_text(OrderFeedLocators.ORDER_NUMBER_TEXT)
        self.wait_for_text_change(OrderFeedLocators.ORDER_NUMBER_TEXT, initial_text)
        return self.get_text(OrderFeedLocators.ORDER_NUMBER_TEXT)

    @allure.step("Проверить наличие заказа в ленте")
    def is_order_in_feed(self, order_id):
        formatted_id = f"{int(order_id):07d}"
        order_locator = OrderFeedLocators.ORDER_NUMBER_IN_LIST
        order_locator = (order_locator[0], order_locator[1].format(formatted_id))
        return self.find_element_with_wait(order_locator)

    @allure.step("Проверить что заказ в работе")
    def is_order_in_progress(self, order_id):
        formatted_id = f"{int(order_id):07d}"
        self.get_dynamic_element(
            OrderFeedLocators.CURRENT_ORDERS_ITEM,
            formatted_id
        )
        return True



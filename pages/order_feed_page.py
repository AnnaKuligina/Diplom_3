from pages.base_page import BasePage
from locators.order_feed_locators import OrderFeedLocators
from curl import FEED_URL

class OrderFeedPage(BasePage):
    def click_last_order(self):
        self.click_on_element(OrderFeedLocators.RECENT_ORDER_CARD)

    def get_order_details_content(self):
        return self.get_text(OrderFeedLocators.ORDER_COMPOSITION_TEXT)

    def get_total_orders_count(self):
        return int(self.get_text(OrderFeedLocators.ALL_TIME_ORDERS_COUNT))

    def get_today_orders_count(self):
        element = self.find_element_with_wait(OrderFeedLocators.TODAY_ORDERS_COUNT)
        return int(element.text.strip())

    def open_feed_page(self):
        self.open_url(FEED_URL)
        self.wait_until_visible(OrderFeedLocators.FEED_HEADER)

    def click_constructor(self):
        self.click_on_element(OrderFeedLocators.CONSTRUCTOR_LINK)

    def click_feed(self):
        self.wait_until_visible(OrderFeedLocators.LOGIN_FORM_TITLE)
        self.click_when_ready(OrderFeedLocators.FEED_LINK)

    def place_order(self):
        self.click_on_element(OrderFeedLocators.MAKE_ORDER_BUTTON)

    def click_account_button(self):
        self.click_when_ready(OrderFeedLocators.PROFILE_LINK)

    def click_order_history(self):
        self.click_on_element(OrderFeedLocators.ORDER_HISTORY_LINK)

    def close_order_details(self):
        self.click_when_ready(OrderFeedLocators.CLOSE_DETAILS_BUTTON)

    def get_order_id(self):
        self.wait_for_text_change(
            OrderFeedLocators.ORDER_NUMBER_TEXT,
            "9999"
        )
        return self.get_text(OrderFeedLocators.ORDER_NUMBER_TEXT)

    def is_order_in_feed(self, order_id):
        formatted_id = f"{int(order_id):07d}"
        order_locator = OrderFeedLocators.ORDER_NUMBER_IN_LIST
        order_locator = (order_locator[0], order_locator[1].format(formatted_id))
        return self.find_element_with_wait(order_locator)

    def is_order_in_progress(self, order_id):
        formatted_id = f"{int(order_id):07d}"
        self.get_dynamic_element(
            OrderFeedLocators.CURRENT_ORDERS_ITEM,
            formatted_id
        )
        return True
# main_page.py
from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators

class MainPage(BasePage):
    def click_constructor(self):
        self.click_on_element(MainPageLocators.CONSTRUCTOR_BUTTON)

    def click_place_order(self):
        self.click_on_element(MainPageLocators.PLACE_ORDER_BUTTON)

    def is_constructor_visible(self):
        return self.is_displayed(MainPageLocators.CONSTRUCTOR_SECTION)

    def click_order_feed(self):
        self.click_on_element(MainPageLocators.ORDER_FEED_BUTTON)

    def is_order_feed_counter_visible(self):
        return self.is_displayed(MainPageLocators.COMPLETED_ORDERS_SECTION)

    def click_ingredient(self):
        self.click_on_element(MainPageLocators.BUN_R2D3)

    def are_ingredient_details_visible(self):
        return self.is_displayed(MainPageLocators.CLOSE_MODAL_BUTTON)

    def close_ingredient_details(self):
        self.click_on_element(MainPageLocators.CLOSE_MODAL_BUTTON)

    def add_ingredient_to_order(self):
        self.click_on_element(MainPageLocators.BUN_R2D3)

    def get_ingredient_counter(self):
        return int(self.get_text(MainPageLocators.INGREDIENT_COUNTER))

    def drag_and_drop_ingredient(self):
        ingredient_locator = MainPageLocators.BUN_R2D3
        target_locator = MainPageLocators.CONSTRUCTOR_TARGET_TOP
        self.drag_and_drop(ingredient_locator, target_locator)

    def get_order_success_message(self):
        return self.get_text(MainPageLocators.ORDER_SUCCESS_NOTIFICATION)
import allure
from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators


class MainPage(BasePage):
    @allure.step("Нажать кнопку 'Конструктор'")
    def click_constructor(self):
        self.click_on_element(MainPageLocators.CONSTRUCTOR_BUTTON)

    @allure.step("Нажать кнопку 'Оформить заказ'")
    def click_place_order(self):
        self.click_on_element(MainPageLocators.PLACE_ORDER_BUTTON)

    @allure.step("Проверить видимость раздела конструктора")
    def is_constructor_visible(self):
        return self.is_displayed(MainPageLocators.CONSTRUCTOR_SECTION)

    @allure.step("Нажать кнопку 'Лента заказов'")
    def click_order_feed(self):
        self.click_on_element(MainPageLocators.ORDER_FEED_BUTTON)

    @allure.step("Проверить видимость счетчика выполненных заказов")
    def is_order_feed_counter_visible(self):
        return self.is_displayed(MainPageLocators.COMPLETED_ORDERS_SECTION)

    @allure.step("Выбрать ингредиент")
    def click_ingredient(self):
        self.click_on_element(MainPageLocators.BUN_R2D3)

    @allure.step("Проверить отображение деталей ингредиента")
    def are_ingredient_details_visible(self):
        return self.is_displayed(MainPageLocators.CLOSE_MODAL_BUTTON)

    @allure.step("Закрыть окно деталей ингредиента")
    def close_ingredient_details(self):
        self.click_on_element(MainPageLocators.CLOSE_MODAL_BUTTON)

    @allure.step("Добавить ингредиент в заказ")
    def add_ingredient_to_order(self):
        self.click_on_element(MainPageLocators.BUN_R2D3)

    @allure.step("Получить значение счетчика ингредиента")
    def get_ingredient_counter(self):
        return int(self.get_text(MainPageLocators.INGREDIENT_COUNTER))

    @allure.step("Перетащить ингредиент в конструктор")
    def drag_and_drop_ingredient(self):
        ingredient_locator = MainPageLocators.BUN_R2D3
        target_locator = MainPageLocators.CONSTRUCTOR_TARGET_TOP
        self.drag_and_drop(ingredient_locator, target_locator)

    @allure.step("Получить сообщение об успешном оформлении заказа")
    def get_order_success_message(self):
        return self.get_text(MainPageLocators.ORDER_SUCCESS_NOTIFICATION)
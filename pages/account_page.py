import allure
from pages.base_page import BasePage
from locators.account_page_locators import AccountPageLocators
from curl import LOGIN_URL


class AccountPage(BasePage):
    @allure.step("Нажать кнопку 'Личный кабинет'")
    def click_account_button(self):
        self.wait_until_visible(AccountPageLocators.BURGER_CONSTRUCTOR_HEADER)
        self.click_when_ready(AccountPageLocators.ACCOUNT_BUTTON)

    @allure.step("Нажать кнопку 'История заказов'")
    def click_order_history_button(self):
        self.click_on_element(AccountPageLocators.ORDER_HISTORY_BUTTON)

    @allure.step("Нажать кнопку 'Выход'")
    def click_logout_button(self):
        self.click_on_element(AccountPageLocators.LOGOUT_BUTTON)

    @allure.step("Проверить видимость кнопки 'Выход'")
    def is_logout_button_visible(self):
        return self.is_visible(AccountPageLocators.LOGOUT_BUTTON)

    @allure.step("Проверить статус заказа 'Выполнен'")
    def is_order_completed(self):
        return self.get_text(AccountPageLocators.COMPLETED_ORDERS_SECTION) == "Выполнен"

    @allure.step("Проверить отображение формы входа после выхода")
    def is_login_form_visible_after_logout(self):
        return self.get_text(AccountPageLocators.LOGIN_FORM_HEADER) == "Вход"

    @allure.step("Открыть страницу входа")
    def open_login_page(self):
        self.open_url(LOGIN_URL)

    @allure.step("Выполнить вход")
    def login(self, email, password):
        self.open_login_page()
        with allure.step("Ввести email"):
            self.input_text(AccountPageLocators.EMAIL_FIELD, email)
        with allure.step("Ввести пароль"):
            self.input_text(AccountPageLocators.PASSWORD_FIELD, password)
        with allure.step("Нажать кнопку входа"):
            self.js_click(AccountPageLocators.LOGIN_FORM_BUTTON)
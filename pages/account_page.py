from pages.base_page import BasePage
from locators.account_page_locators import AccountPageLocators
from curl import LOGIN_URL

class AccountPage(BasePage):
    def click_account_button(self):
        self.wait_until_visible(AccountPageLocators.BURGER_CONSTRUCTOR_HEADER)
        self.click_when_ready(AccountPageLocators.ACCOUNT_BUTTON)

    def click_order_history_button(self):
        self.click_on_element(AccountPageLocators.ORDER_HISTORY_BUTTON)

    def click_logout_button(self):
        self.click_on_element(AccountPageLocators.LOGOUT_BUTTON)

    def is_logout_button_visible(self):
        return self.is_visible(AccountPageLocators.LOGOUT_BUTTON)

    def is_order_completed(self):
        return self.get_text(AccountPageLocators.COMPLETED_ORDERS_SECTION) == "Выполнен"

    def is_login_form_visible_after_logout(self):
        return self.get_text(AccountPageLocators.LOGIN_FORM_HEADER) == "Вход"

    def open_login_page(self):
        self.open_url(LOGIN_URL)

    def login(self, email, password):
        self.open_login_page()
        self.input_text(AccountPageLocators.EMAIL_FIELD, email)
        self.input_text(AccountPageLocators.PASSWORD_FIELD, password)
        self.js_click(AccountPageLocators.LOGIN_FORM_BUTTON)
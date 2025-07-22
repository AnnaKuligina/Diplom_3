from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import ElementClickInterceptedException
import allure

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step("Поиск элемента")
    def find_element_with_wait(self, locator, timeout=10):
        WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator)
        )
        return self.driver.find_element(*locator)

    @allure.step("Клик по элементу")
    def click_on_element(self, locator, timeout=20):
        element = WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable(locator)
        )
        actions = ActionChains(self.driver)
        actions.move_to_element(element).click().perform()

    @allure.step("Ввод текста")
    def input_text(self, locator, text):
        self.find_element_with_wait(locator).send_keys(text)

    @allure.step("Получение текста из элемента")
    def get_text(self, locator):
        return self.find_element_with_wait(locator).text

    @allure.step("Скролл к элементу")
    def scroll_to_element(self, locator):
        element = self.find_element_with_wait(locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    @allure.step("Форматирование локатора")
    def format_locator(self, locator, value):
        method, locator_template = locator
        formatted_locator = locator_template.format(value)
        return method, formatted_locator

    @allure.step("Клик по элементу с ожиданием кликабельности")
    def click_when_ready(self, locator, timeout=20):
        WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable(locator)
        )
        self.driver.find_element(*locator).click()

    @allure.step("Проверка видимости элемента")
    def is_visible(self, locator, timeout=20):
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located(locator))
            return True
        except TimeoutException:
            return False

    @allure.step("Клик через JavaScript")
    def js_click(self, locator, timeout=20):
        element = WebDriverWait(self.driver, timeout).until(
            EC.presence_of_element_located(locator)
        )
        self.driver.execute_script("arguments[0].click();", element)

    @allure.step("Ожидание видимости элемента")
    def wait_until_visible(self, locator, timeout=10):
        WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator)
        )

    @allure.step("Перетаскивание элемента")
    def drag_and_drop(self, source_locator, target_locator):

        self.find_element_with_wait(source_locator)
        self.find_element_with_wait(target_locator)

        element_from = self.driver.find_element(*source_locator)
        element_to = self.driver.find_element(*target_locator)

        self.driver.execute_script("""
            var source = arguments[0];
            var target = arguments[1];

            var evt = document.createEvent("DragEvent");
            evt.initMouseEvent("dragstart", true, true, window, 0, 0, 0, 0, 0, false, false, false, false, 0, null);
            source.dispatchEvent(evt);

            evt = document.createEvent("DragEvent");
            evt.initMouseEvent("dragenter", true, true, window, 0, 0, 0, 0, 0, false, false, false, false, 0, null);
            target.dispatchEvent(evt);

            evt = document.createEvent("DragEvent");
            evt.initMouseEvent("dragover", true, true, window, 0, 0, 0, 0, 0, false, false, false, false, 0, null);
            target.dispatchEvent(evt);

            evt = document.createEvent("DragEvent");
            evt.initMouseEvent("drop", true, true, window, 0, 0, 0, 0, 0, false, false, false, false, 0, null);
            target.dispatchEvent(evt);

            evt = document.createEvent("DragEvent");
            evt.initMouseEvent("dragend", true, true, window, 0, 0, 0, 0, 0, false, false, false, false, 0, null);
            source.dispatchEvent(evt);
        """, element_from, element_to)

    @allure.step("Проверка отображения элемента")
    def is_displayed(self, locator):
        try:
            element = self.find_element_with_wait(locator)
            return element.is_displayed()
        except TimeoutException:
            return False

    @allure.step("Открытие URL")
    def open_url(self, url):
        self.driver.get(url)

    @allure.step("Ожидание условия")
    def wait_for(self, condition, timeout=20):
        WebDriverWait(self.driver, timeout).until(condition)

    @allure.step("Ожидание изменения текста в элементе")
    def wait_for_text_change(self, locator, initial_text, timeout=20):
        self.wait_for(
            lambda _: self.get_text(locator) != initial_text, timeout
        )
        return self.find_element_with_wait(locator)

    @allure.step("Получение динамического элемента")
    def get_dynamic_element(self, locator, dynamic_value):
        formatted_locator = self.format_locator(locator, dynamic_value)
        return self.find_element_with_wait(formatted_locator)

    @allure.step("Получение атрибута элемента")
    def get_attribute(self, locator, attribute_name):
        element = self.find_element_with_wait(locator)
        return element.get_attribute(attribute_name)

    @allure.step("Ожидание исчезновения элемента")
    def wait_invisibility(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.invisibility_of_element_located(locator)
        )

    @allure.step("Закрытие модального окна")
    def safe_close_modal(self, close_button_locator, overlay_locator=None, timeout=15):
        try:
            if overlay_locator:
                self.wait_invisibility(overlay_locator, timeout)

            try:
                self.click_on_element(close_button_locator)
            except ElementClickInterceptedException:
                self.js_click(close_button_locator)

            if overlay_locator:
                self.wait_invisibility(overlay_locator, timeout)
            return True

        except Exception as e:
            allure.attach(
                body=self.driver.get_screenshot_as_png(),
                name=f"modal_close_failure_{close_button_locator}",
                attachment_type=allure.attachment_type.PNG
            )
            return False
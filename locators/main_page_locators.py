from selenium.webdriver.common.by import By


class MainPageLocators:
    # Конструктор
    CONSTRUCTOR_BUTTON = (By.XPATH, "//p[contains(text(),'Конструктор')]")
    CONSTRUCTOR_SECTION = (By.XPATH, "//section[@class='BurgerIngredients_ingredients__1N8v2']")

    # Лента заказов
    ORDER_FEED_BUTTON = (By.XPATH, "//p[contains(text(),'Лента Заказов')]")
    COMPLETED_ORDERS_SECTION = (By.XPATH, "//p[contains(text(),'Готовы:')]")
    TOTAL_ORDERS_COUNTER = (By.XPATH, "//p[normalize-space()='153072']")

    # Ингредиенты
    BUN_R2D3 = (By.XPATH, "//img[@alt='Флюоресцентная булка R2-D3']")
    INGREDIENT_DETAILS_MODAL = (By.XPATH, "//h2[@class='Modal_modal__title_modified__3Hjkd Modal_modal__title__2L34m text text_type_main-large pl-10']")
    CLOSE_MODAL_BUTTON = (By.XPATH, "//section[@class='Modal_modal_opened__3ISw4 Modal_modal__P3_V5']//button[@type='button']//*[name()='svg']//*[name()='path' and contains(@fill-rule,'evenodd')]")

    # Конструктор заказов
    CONSTRUCTOR_TARGET_TOP = (By.XPATH, "//img[@alt='Перетяните булочку сюда (верх)']")
    INGREDIENT_COUNTER = (By.XPATH, "//p[@class='counter_counter__num__3nue1']")
    PLACE_ORDER_BUTTON = (By.XPATH, "//button[@class='button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_large__G21Vg']")

    # Статус заказа
    ORDER_SUCCESS_NOTIFICATION = (By.XPATH, "//p[@class='undefined text text_type_main-small mb-2']")
    ORDER_IN_PROGRESS_ITEM = (By.XPATH,  "//ul[@class='OrderFeed_orderListReady__1YFem OrderFeed_orderList__cBvyi']//li[1]//*[contains(text(), '{0}')]")
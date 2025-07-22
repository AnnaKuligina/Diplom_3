from selenium.webdriver.common.by import By


class OrderFeedLocators:
    # Кнопка "Оформить заказ" на странице конструктора
    MAKE_ORDER_BUTTON = (By.XPATH, "//button[contains(@class, 'button_button_type_primary')]")
    # Ссылка "Лента Заказов" в шапке приложения
    FEED_LINK = (By.XPATH, "//a[contains(@href,'/feed')]")
    # Ссылка "Конструктор" в шапке приложения
    CONSTRUCTOR_LINK = (By.XPATH, "//p[text()='Конструктор']")
    #Статус заказа в модальном окне
    ORDER_STATUS_TEXT = (By.XPATH, "//p[contains(@class, 'text_type_main-default') and text()='Выполнен']")
    # Ссылка "История заказов" в личном кабинете
    ORDER_HISTORY_LINK = (By.XPATH, "//a[contains(@class, 'Account_link__2ETsJ')]")
    # Ссылка "Личный Кабинет" в шапке приложения
    PROFILE_LINK = (By.XPATH, "//p[text()='Личный Кабинет']")
    # Карточка последнего созданного заказа в ленте
    RECENT_ORDER_CARD = (By.XPATH, ".//li[contains(@class, 'listItem')][1]")
    # Текст с составом заказа в модальном окне
    ORDER_COMPOSITION_TEXT = (By.XPATH, "//p[@class='text text_type_main-medium mb-8']")
    # Счетчик "Выполнено за все время" на главной странице
    ALL_TIME_ORDERS_COUNT = (By.XPATH, '//p[text()="Выполнено за все время:"]/following-sibling::p')
    # Счетчик "Выполнено за сегодня" на главной странице
    TODAY_ORDERS_COUNT = (By.XPATH, '//p[text()="Выполнено за сегодня:"]/following-sibling::p')
    # Кнопка закрытия всплывающего окна крестиком
    CLOSE_DETAILS_BUTTON = (By.XPATH, "//button[@type='button']//*[name()='svg']")
    # Номер заказа во всплывающем окне
    ORDER_NUMBER_TEXT = (By.XPATH, "//h2[contains(@class, 'Modal_modal__title')]")
    # Номер заказа в списке
    ORDER_NUMBER_IN_LIST = (By.XPATH, "//*[contains(text(), '{0}')]")
    # Первый заказ в разделе "В работе"
    CURRENT_ORDERS_ITEM = (By.XPATH, '//ul[contains(@class, "OrderFeed_orderListReady")]/li')
    # Заголовок "Лента заказов"
    FEED_HEADER = (By.XPATH, "//h1[contains(@class, 'text_type_main-large')]")
    # Заголовок формы авторизации
    LOGIN_FORM_TITLE = (By.XPATH, "//h1[text()='Вход']")
    # Текст "Готовим ваш заказ" в появляющемся окне
    ORDER_IN_PROGRESS_TEXT = (By.XPATH, "//p[contains(text(), 'Готовим ваш заказ')]")
    # Оверлей всплывающего окна
    LOADING_OVERLAY = (By.XPATH, "//div[@class='Modal_modal_opened__3ISw4 Modal_modal__P3_V5']//div[@class='Modal_modal_overlay__x2ZCr']")


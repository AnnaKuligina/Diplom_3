from selenium.webdriver.common.by import By


class OrderFeedLocators:
    # Кнопка "Оформить заказ" на странице конструктора
    MAKE_ORDER_BUTTON = (By.XPATH, "//button[@class='button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_large__G21Vg']")
    # Ссылка "Лента Заказов" в шапке приложения
    FEED_LINK = (By.XPATH, "//p[contains(text(),'Лента Заказов')]")
    # Ссылка "Конструктор" в шапке приложения
    CONSTRUCTOR_LINK = (By.XPATH, "//p[contains(text(),'Конструктор')]")
    # Ссылка "История заказов" в личном кабинете
    ORDER_HISTORY_LINK = (By.XPATH, "//a[@class='Account_link__2ETsJ text text_type_main-medium text_color_inactive']")
    # Ссылка "Личный Кабинет" в шапке приложения
    PROFILE_LINK = (By.XPATH, "//p[contains(text(),'Личный Кабинет')]")
    # Карточка последнего созданного заказа в ленте
    RECENT_ORDER_CARD = (By.XPATH, "//body/div[@id='root']/div[@class='App_App__aOmNj']/main[@class='App_componentContainer__2JC2W']/div[@class='OrderFeed_orderFeed__2RO_j']/div[@class='OrderFeed_contentBox__3-tWb']/ul[@class='OrderFeed_list__OLh59']/li[1]/a[1]/div[1]")
    # Текст с составом заказа в модальном окне
    ORDER_COMPOSITION_TEXT = (By.XPATH, "//p[@class='text text_type_main-medium mb-8']")
    # Счетчик "Выполнено за все время" на главной странице
    ALL_TIME_ORDERS_COUNT = (By.XPATH, "//div[@class='undefined mb-15']//p[contains(@class, 'OrderFeed_number__2MbrQ') and normalize-space(text())]")
    # Счетчик "Выполнено за сегодня" на главной странице
    TODAY_ORDERS_COUNT = (By.XPATH,"//p[@class='OrderFeed_number__2MbrQ text text_type_digits-large']")
    # Кнопка закрытия всплывающего окна крестиком
    CLOSE_DETAILS_BUTTON = (By.XPATH, "//button[@type='button']//*[name()='svg']")
    # Номер заказа во всплывающем окне
    ORDER_NUMBER_TEXT = (By.XPATH, "//h2[contains(@class, 'Modal_modal__title') and normalize-space(text())]")
    # Номер заказа в списке
    ORDER_NUMBER_IN_LIST = (By.XPATH, "//*[contains(text(), '{0}')]")
    # Первый заказ в разделе "В работе"
    CURRENT_ORDERS_ITEM = (By.XPATH, "//ul[contains(@class, 'OrderFeed_orderList')]/li[1]")
    # Заголовок "Лента заказов"
    FEED_HEADER = (By.XPATH, "//h1[contains(@class, 'text_type_main-large')]")
    # Заголовок формы авторизации
    LOGIN_FORM_TITLE = ( By.XPATH, "//h1[@class='text text_type_main-large mb-5 mt-10']")
    # Текст "Готовим ваш заказ" в появляющемся окне
    ORDER_IN_PROGRESS_TEXT = (By.XPATH, "//p[@class='undefined text text_type_main-small mb-2']")
    # Оверлей всплывающего окна
    LOADING_OVERLAY = (By.XPATH, "//div[@class='Modal_modal_opened__3ISw4 Modal_modal__P3_V5']//div[@class='Modal_modal_overlay__x2ZCr']")
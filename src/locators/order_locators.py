from selenium.webdriver.common.by import By


class OrderLocators:
    FIRSTNAME_FIELD = By.XPATH, "//input[@placeholder='* Имя']"
    LASTNAME_FIELD = By.XPATH, "//input[@placeholder='* Фамилия']"
    ADDRESS_FIELD = By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']"
    METRO_STATION_FIELD = By.XPATH, ".//li[@data-index='1']"
    METRO_FIELD = By.XPATH, "//div[4]"
    NUMBER_FIELD = By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']"
    NEXT_BUTTON = By.XPATH, "//button[@class='Button_Button__ra12g Button_Middle__1CSJM']"
    DATE_ORDER_FIELD = By.XPATH, "//div[@class='Order_MixedDatePicker__3qiay']"
    DATE_ORDER = By.XPATH, "//div[@class='react-datepicker__day react-datepicker__day--028']"
    RENTAL_PERIOD_FIELD = By.XPATH, "//div[@class='Dropdown-root']"
    RENTAL_PERIOD = By.XPATH, "//div[@class='Dropdown-option']"
    CONFIRM_BUTTON = By.XPATH, "//button[@class='Button_Button__ra12g Button_Middle__1CSJM']"
    STATUS_BUTTON = By.XPATH, "//div[@class='Order_Modal__YZ-d3']/div/button[@class='Button_Button__ra12g Button_Middle__1CSJM']"
    SUCCESSFUL_ORDER_POPUP = By.XPATH, "//div[@class='Order_Modal__YZ-d3']"
from src.locators.order_locators import OrderLocators
from src.pages.base_page import BasePage
from selenium.webdriver.common.by import By
from src.helpers import reg_new_user, telephone_number
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class OrderPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def enter_order_data(self):
        firstname_data, lastname_data, address_data, email_data, password_data = reg_new_user()
        number_data = telephone_number()
        self.find_element(OrderLocators.FIRSTNAME_FIELD).send_keys(firstname_data)
        self.find_element(OrderLocators.LASTNAME_FIELD).send_keys(lastname_data)
        self.find_element(OrderLocators.ADDRESS_FIELD).send_keys(address_data)
        self.click_element(OrderLocators.METRO_FIELD)
        self.click_element(OrderLocators.METRO_STATION_FIELD)
        self.find_element(OrderLocators.NUMBER_FIELD).send_keys(number_data)
        self.click_element(OrderLocators.NEXT_BUTTON)
        self.click_element(OrderLocators.DATE_ORDER_FIELD)
        self.click_element(OrderLocators.DATE_ORDER)
        self.click_element(OrderLocators.RENTAL_PERIOD_FIELD)
        self.click_element(OrderLocators.RENTAL_PERIOD)
        self.click_element(OrderLocators.CONFIRM_BUTTON)
        self.click_element(OrderLocators.STATUS_BUTTON)

    def successful_order_popup_is_displayed(self):
        successful_order_popup = self.find_element(OrderLocators.SUCCESSFUL_ORDER_POPUP)
        return successful_order_popup.is_displayed()
import time

import pytest
from src.pages.main_page import MainPage
from src.pages.order_page import OrderPage
from src.config import Config
from src.locators.main_page_locators import MainPageLocators
from allure import title, step


class TestScooterOrder:
    @title("Test scooter order")
    @pytest.mark.parametrize("order_locator",
                             [MainPageLocators.HEADER_BUTTON_ORDER, MainPageLocators.FOOTER_BUTTON_ORDER])
    def test_successful_order(self, driver, order_locator):
        order_button = MainPage(driver)
        order_button.navigate(Config.URL)
        order_button.order_button_click(order_locator)
        order = OrderPage(driver)
        order.enter_order_data()
        assert order.successful_order_popup_is_displayed() is True

    def test_click_logo_button(self, driver):
        logo_button = MainPage(driver)
        logo_button.navigate(Config.ORDER_URL)
        logo_button.logo_button_click()
        assert logo_button.get_current_url() == Config.SCOOTER_URL

    def test_click_logo_yandex(self, driver):
        logo_yandex = MainPage(driver)
        logo_yandex.navigate(Config.URL)
        logo_yandex.logo_yandex_click()
        driver.switch_to.window(driver.window_handles[1])
        time.sleep(5)
        assert logo_yandex.get_current_url() == Config.YANDEX_URL

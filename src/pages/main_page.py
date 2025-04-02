import pytest
from selenium.webdriver.support.ui import WebDriverWait
from src.locators.main_page_locators import MainPageLocators
from src.pages.base_page import BasePage
from selenium.webdriver.common.by import By
from allure import step


class MainPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def open_page(self, url):
        with step(f'Open page {url}'):
            self.navigate(url)

    def click_on_questions(self, locator):
        with step(f'Click on question'):
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
            self.wait_for_element_clickable(locator).click()

    def get_answer(self, locator):
        with step(f'Get answer'):
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
            answer = self.select_element(locator)
            return answer.is_displayed()

    def order_button_click(self, locator):
        with step(f'Click order button'):
            self.click_element(MainPageLocators.COOKIE_BUTTON)
            self.wait_for_element_visibility(locator).click()

    def logo_button_click(self):
        with step(f'Click logo scooter'):
            self.click_element(MainPageLocators.LOGO_BUTTON)

    def logo_yandex_click(self):
        with step(f'Click logo yandex'):
            self.click_element(MainPageLocators.LOGO_YANDEX_BUTTON)

    def get_current_url(self):
        with step(f'Current url'):
            return self.driver.current_url
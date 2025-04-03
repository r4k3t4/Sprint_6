import pytest
from selenium.webdriver.support.ui import WebDriverWait
from src.locators.main_page_locators import MainPageLocators
from src.pages.base_page import BasePage
from selenium.webdriver.common.by import By
import allure


class MainPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    @allure.step(f'Open page')
    def open_page(self, url):
        self.navigate(url)

    @allure.step(f'Click on question')
    def click_on_questions(self, locator):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
        self.wait_for_element_clickable(locator).click()

    @allure.step(f'Get answer')
    def get_answer(self, locator):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
        answer = self.select_element(locator)
        return answer.is_displayed()

    @allure.step(f'Click order button')
    def order_button_click(self, locator):
        self.click_element(MainPageLocators.COOKIE_BUTTON)
        self.wait_for_element_visibility(locator).click()

    @allure.step(f'Click logo scooter')
    def logo_button_click(self):
        self.click_element(MainPageLocators.LOGO_BUTTON)

    @allure.step(f'Click logo yandex')
    def logo_yandex_click(self):
        self.click_element(MainPageLocators.LOGO_YANDEX_BUTTON)

    @allure.step(f'Current url')
    def get_current_url(self):
        return self.driver.current_url
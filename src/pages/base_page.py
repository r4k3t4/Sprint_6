from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.common.exceptions import TimeoutException
import allure


class BasePage:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def navigate(self, url):
        with allure.step(f"Open page {url}"):
            self.driver.get(url)

    def find_element(self, locator):
        with allure.step(f"Find element with locator {locator}"):
            return WebDriverWait(self.driver, timeout=15).until(EC.presence_of_element_located(locator))

    def click_element(self, locator):
        with allure.step(f"Click element with locator {locator}"):
            self.find_element(locator).click()

    def select_element(self, locator):
        with allure.step(f"Find element with locator {locator}"):
            return WebDriverWait(self.driver, timeout=10).until(EC.presence_of_element_located(locator))

    def wait_for_element_clickable(self, locator, timeout=10):
        with allure.step(f"Find element with locator {locator}"):
            return WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable(locator))

    def wait_for_element_visibility(self, locator, timeout=10):
        with allure.step(f"Find element with locator {locator}"):
            return WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))








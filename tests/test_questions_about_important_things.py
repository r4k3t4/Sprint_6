import pytest
from src.pages.main_page import MainPage
from src.pages.base_page import BasePage
from src.config import Config
from src.locators.main_page_locators import MainPageLocators
from allure import title, step


class TestScooterImportantQuestions:
    @title("Test important questions")
    @pytest.mark.parametrize("number", ["0", "1", "2", "3", "4", "5", "6", "7"])
    def test_click_important_questions(self, driver, number):
        questions = MainPage(driver)
        questions.navigate(Config.URL)
        questions.click_on_questions(MainPageLocators.questions(number))
        assert questions.get_answer(MainPageLocators.answers(number)) is True

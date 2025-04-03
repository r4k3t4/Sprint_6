from selenium.webdriver.common.by import By

class MainPageLocators:

    HEADER_BUTTON_ORDER = By.XPATH, "//button[@class='Button_Button__ra12g']"
    FOOTER_BUTTON_ORDER = By.XPATH, "//button[@class='Button_Button__ra12g Button_UltraBig__UU3Lp']"
    LOGO_BUTTON = By.XPATH, "//a[@class='Header_LogoScooter__3lsAR']"
    COOKIE_BUTTON = By.XPATH, "//button[@class='App_CookieButton__3cvqF']"
    LOGO_YANDEX_BUTTON = By.XPATH, "//a[@class='Header_LogoYandex__3TSOI']"

    @staticmethod
    def questions(number):
        MainPageLocators.QUESTIONS = By.XPATH, f".//div[@id='accordion__heading-{number}']"
        return MainPageLocators.QUESTIONS

    @staticmethod
    def answers(number):
        MainPageLocators.ANSWERS = By.XPATH, f"//div[@id='accordion__panel-{number}']"
        return MainPageLocators.ANSWERS

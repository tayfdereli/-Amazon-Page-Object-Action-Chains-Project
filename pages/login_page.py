from pages.base_page import BasePage
from utils.locators import LoginPageLocators


class LoginPage(BasePage):
    def __init__(self, driver):
        self.locator = LoginPageLocators
        super().__init__(driver)

    def sign_in(self):
        self.fill(self.locator.E_MAIL_ADRESS, *self.locator.E_MAIL)
        self.click(*self.locator.E_MAIL_SUBMIT)
        self.fill(self.locator.E_MAIL_PASSWORD, *self.locator.PASSWORD)
        self.click(*self.locator.SIGN_IN_SUBMIT)


from pages.base_page import BasePage
from utils.locators import HomePageLocators


class HomePage(BasePage):
    def __init__(self, driver):
        self.locator = HomePageLocators
        super().__init__(driver)

    def go_to_sign_in(self):
        self.click(*self.locator.DONT_CHANGE_BUTTON)
        self.click(*self.locator.NO_THANKS_BUTTON)
        self.click(*self.locator.SIGN_IN_BUTTON)

    def search_keyword(self):
        self.fill(self.locator.SEARCH_KEYWORD, *self.locator.SEARCH_BOX)
        self.click(*self.locator.SEARCH_BOX_BUTTON)

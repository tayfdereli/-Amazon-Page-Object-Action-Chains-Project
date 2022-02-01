from pages.base_page import BasePage
from utils.locators import ProductPageLocators, SearchPageLocators


class ProductPage(BasePage):

    def __init__(self, driver):
        self.locator = ProductPageLocators
        self.search_page_locator = SearchPageLocators
        super().__init__(driver)

    def add_to_wish_list(self):
        self.click(*self.locator.WIEW_YOUR_LIST_BUTTON)

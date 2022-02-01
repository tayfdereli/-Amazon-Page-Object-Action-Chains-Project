from pages.base_page import BasePage
from pages.search_page import SearchPage
from utils.locators import SearchPageLocators, WishListPageLocators


class WishListPage(BasePage):

    def __init__(self, driver):
        self.search_page = SearchPage(driver)
        self.locator = WishListPageLocators
        self.search_page_locator = SearchPageLocators
        super().__init__(driver)

    def remove_product_in_wish_list(self):
        self.click(*self.locator.DELETE_BUTTON)

    def is_the_wish_list_empty(self):
        assert "Deleted" == self.visibility_element(self.locator.DELETED_TEXT).text

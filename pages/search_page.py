from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from utils.locators import SearchPageLocators, ProductPageLocators


class SearchPage(BasePage):
    product = ""

    def __init__(self, driver):
        self.locator = SearchPageLocators
        self.product_page_locators = ProductPageLocators
        super().__init__(driver)

    def keyword_control(self):
        assert "Samsung" in self.find_element(*self.locator.SEARCH_KEYWORD_CONTROL).text

    def go_to_second_page(self):
        self.click(*self.locator.SECOND_PAGE)
        assert "page=2" in self.get_url()

    def choose_the_third_product(self):
        self.product = self.driver.find_elements(*self.locator.THIRD_PRODUCT)[2].text
        self.click(By.XPATH, "//span[text()='" + self.product + "']")
        self.click(*self.product_page_locators.ADD_TO_LIST_BUTTON)

    def check_product_in_wish_list(self):
        assert self.product == self.find_element(*self.locator.THIRD_PRODUCT).text

from selenium.webdriver.common.by import By


class HomePageLocators(object):
    BASE_URL = "https://www.amazon.com/"
    SIGN_IN_BUTTON = (By.ID, "nav-link-accountList")
    NO_THANKS_BUTTON = (By.ID, "aaee-xop-dismiss")
    DONT_CHANGE_BUTTON = (By.CSS_SELECTOR, ".a-button-inner:nth-child(1)")
    SEARCH_BOX = (By.ID, "twotabsearchtextbox")
    SEARCH_KEYWORD = "Samsung"
    SEARCH_BOX_BUTTON = (By.ID, "nav-search-submit-button")


class LoginPageLocators(object):
    E_MAIL_ADRESS = "yourmailadress"
    E_MAIL_PASSWORD = "yourpassword"
    E_MAIL = (By.ID, "ap_email")
    E_MAIL_SUBMIT = (By.ID, "continue")
    PASSWORD = (By.ID, "ap_password")
    SIGN_IN_SUBMIT = (By.ID, "signInSubmit")


class ProductPageLocators(object):
    ADD_TO_LIST_BUTTON = (By.ID, "add-to-wishlist-button-submit")
    WIEW_YOUR_LIST_BUTTON = (By.ID, "WLHUC_viewlist")


class WishListPageLocators(object):
    DELETE_BUTTON = (By.NAME, "submit.deleteItem")
    DELETED_TEXT = (By.CSS_SELECTOR, ".a-alert-inline-success .a-alert-content")


class SearchPageLocators(object):
    SEARCH_KEYWORD_CONTROL = (By.CLASS_NAME, "a-color-state")
    SECOND_PAGE = (By.CLASS_NAME, "s-pagination-button")
    THIRD_PRODUCT = (By.TAG_NAME, "h2")

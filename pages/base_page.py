from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class BasePage(object):
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)
        self.driver.implicitly_wait(15)

    def find_element(self, *locator):
        return self.driver.find_element(*locator)

    def get_title(self):
        return self.driver.title

    def get_url(self):
        return self.driver.current_url

    def visibility_element(self, *locator):
        return self.wait.until(EC.visibility_of_element_located(*locator))

    def fill(self, text, *locator):
        self.find_element(*locator).send_keys(text)

    def click(self, *locator):
        self.find_element(*locator).click()

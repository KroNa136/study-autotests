from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    url = None

    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    def open(self):
        if not self.url:
            raise ValueError(f"URL not set for the page {self.__class__.__name__}")
        self.driver.get(self.url)

    def find(self, by, locator):
        return self.driver.find_element(by, locator)

    def wait_for_present(self, by, locator):
        return self.wait.until(
            EC.presence_of_element_located((by, locator))
        )

    def is_element_present(self, by, locator):
        try:
            self.driver.find_element(by, locator)
            return True
        except Exception:
            return False

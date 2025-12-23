from selenium.webdriver.common.by import By
from base_page import BasePage

class FeedbackPage(BasePage):
    url = "http://127.0.0.1:8000/index.php"

    NAME_INPUT = (By.ID, "name-input")
    EMAIL_INPUT = (By.ID, "email-input")
    MESSAGE_TEXTAREA = (By.ID, "message-textarea")
    SUBMIT_BUTTON = (By.ID, "submit-button")

    SUCCESS_MESSAGE = (By.ID, "success-message")
    ERROR_MESSAGE = (By.ID, "error-message")

    def fill_name(self, name):
        field = self.find(*self.NAME_INPUT)
        field.clear()
        field.send_keys(name)

    def fill_email(self, email):
        field = self.find(*self.EMAIL_INPUT)
        field.clear()
        field.send_keys(email)

    def fill_message(self, message):
        field = self.find(*self.MESSAGE_TEXTAREA)
        field.clear()
        field.send_keys(message)

    def submit(self):
        self.find(*self.SUBMIT_BUTTON).click()

    def send_feedback(self, name, email, message):
        self.fill_name(name)
        self.fill_email(email)
        self.fill_message(message)
        self.submit()

    def wait_for_success_message(self):
        return self.wait_for_present(*self.SUCCESS_MESSAGE)

    def wait_for_error_message(self):
        return self.wait_for_present(*self.ERROR_MESSAGE)

    def get_success_message_text(self):
        element = self.wait_for_success_message()
        return element.text

    def get_error_message_text(self):
        element = self.wait_for_error_message()
        return element.text

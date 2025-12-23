from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from feedback_page import FeedbackPage

driver = webdriver.Edge()

try:
    feedbackPage = FeedbackPage(driver)
    feedbackPage.open()
    feedbackPage.send_feedback("Alice", "alice@gmail.com", "Some message for the feedback form.")
    message = feedbackPage.get_success_message_text()
    print(message)
except TimeoutException:
    print("timeout")
finally:
    driver.quit()

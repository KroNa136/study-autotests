from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.options import Options
from feedback_page import FeedbackPage

def test_positive_case():
    options = Options()
    options.add_argument("--headless=new")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-gpu")

    driver = webdriver.Chrome(options=options)

    try:
        feedback_page = FeedbackPage(driver)
        feedback_page.open()
        feedback_page.send_feedback("Alice", "alice@gmail.com", "Some message for the feedback form.")
        message = feedback_page.get_success_message_text()
        print(message)
    except TimeoutException:
        print("timeout")
    finally:
        driver.quit()

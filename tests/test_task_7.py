from selenium.webdriver.common.by import By
from selenium.webdriver.support.expected_conditions import text_to_be_present_in_element
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

from pages.main_page import MainPage


def test_wait(browser):
    page = MainPage(browser)
    page.open("http://suninjuly.github.io/explicit_wait2.html")

    # Ожидаем, когда кнопка с ID 'book' станет кликабельной
    WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100")
    )
    browser.find_element(By.ID, "book").click()

    x = page.get_input_value()
    result = page.calculate_answer(x)
    page.enter_answer(result)
    page.submit()

    alert_text = page.accept_alert()
    print(f"✅ Результат из окна: {alert_text}")
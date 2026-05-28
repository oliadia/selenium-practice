from pages.main_page import MainPage

def test_file_upload(browser):
    page = MainPage(browser)

    page.open("http://suninjuly.github.io/alert_accept.html")
    page.submit()
    alert = browser.switch_to.alert
    alert.accept()
    x = page.get_input_value()
    result = page.calculate_answer(x)
    page.enter_answer(result)
    page.submit()

    alert_text = page.accept_alert()
    print(f"✅ Результат из окна: {alert_text}")

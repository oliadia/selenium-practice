from pages.main_page import MainPage

def test_window_switch(browser):
    page = MainPage(browser)
    page.open("http://suninjuly.github.io/redirect_accept.html")
    page.submit()
    first_window = browser.window_handles[0]
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)
    x = page.get_input_value()
    result = page.calculate_answer(x)
    page.enter_answer(result)
    page.submit()

    alert_text = page.accept_alert()
    print(f"✅ Результат из окна: {alert_text}")
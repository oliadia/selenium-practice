from pages.main_page import MainPage


def test_javascript(browser):
    page = MainPage(browser)

    page.open("https://suninjuly.github.io/execute_script.html")

    x = page.get_input_value()
    result = page.calculate_answer(x)

    page.enter_answer(result)
    page.click_robot_checkbox()
    page.click_robots_radio()
    page.submit()

    alert_text = page.accept_alert()
    print(f"✅ Результат из окна: {alert_text}")
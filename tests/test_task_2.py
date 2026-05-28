import pytest

from pages.main_page import MainPage


@pytest.mark.usefixtures("browser")
@pytest.mark.parametrize("url", [
    "https://suninjuly.github.io/selects1.html",
    "https://suninjuly.github.io/selects2.html",
])
def test_dropdown(browser, url):
    page = MainPage(browser)

    page.open(url)

    result = page.get_sum()
    page.select_sum_in_dropdown(result)
    page.submit()

    alert_text = page.accept_alert()
    print(f"Сообщение из всплывающего окна: {alert_text}")
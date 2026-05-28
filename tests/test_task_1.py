import pytest

from pages.main_page import MainPage


@pytest.mark.usefixtures("browser")
def test_treasure_chest(browser):
    page = MainPage(browser)

    page.open("http://suninjuly.github.io/get_attribute.html")

    x = page.get_treasure_value()
    result = page.calculate_answer(x)

    page.enter_answer(result)
    page.click_robot_checkbox()
    page.click_robots_radio()
    page.submit()
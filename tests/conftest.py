import pytest
from selenium import webdriver


@pytest.fixture
def browser():
    """Создает браузер перед тестом и закрывает после него."""
    print("\nЗапускаю браузер для теста...")

    driver = webdriver.Chrome()
    driver.maximize_window()

    try:
        yield driver
    finally:
        print("\nЗакрываю браузер.")
        driver.quit()
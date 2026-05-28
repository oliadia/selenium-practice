from pathlib import Path

from pages.main_page import MainPage

def test_file_upload(browser):
    page = MainPage(browser)

    page.open("https://suninjuly.github.io/file_input.html")
    file_path = Path(__file__).parent / "files/test_file.txt"

    page.fill_registration_form("Иван",
                                "Иванов",
                                "ivan@example.com",
                                file_path)

    page.submit()

    alert_text = page.accept_alert()
    print(f"✅ Результат из окна: {alert_text}")
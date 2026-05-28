import math

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class MainPage:
    """Page Object для учебных страниц suninjuly.github.io."""

    TREASURE_IMG = (By.ID, "treasure")
    ANSWER_INPUT = (By.ID, "answer")
    ROBOT_CHECKBOX = (By.ID, "robotCheckbox")
    ROBOTS_RADIO = (By.ID, "robotsRule")
    SUBMIT_BTN = (By.CSS_SELECTOR, "button[type='submit']")

    NUM1 = (By.ID, "num1")
    NUM2 = (By.ID, "num2")
    DROPDOWN_SELECT = (By.ID, "dropdown")
    INPUT_VALUE = (By.ID, "input_value")

    FIRST_NAME_INPUT = (By.NAME, "firstname")
    LAST_NAME_INPUT = (By.NAME, "lastname")
    EMAIL_INPUT = (By.NAME, "email")
    FILE_INPUT = (By.ID, "file")

    def __init__(self, driver):
        self.driver = driver

    def open(self, url):
        """Открывает страницу по URL."""
        self.driver.get(url)

    @staticmethod
    def calculate_answer(x):
        """Вычисляет значение по формуле ln(abs(12 * sin(x)))."""
        return math.log(abs(12 * math.sin(x)))

    def find_element(self, locator):
        """Находит элемент по локатору."""
        return self.driver.find_element(*locator)

    def scroll_to_element(self, element):
        """Прокручивает страницу к элементу."""
        self.driver.execute_script(
            "arguments[0].scrollIntoView({block: 'center'});",
            element,
        )

    def click_with_js(self, element):
        """Кликает по элементу через JavaScript."""
        self.driver.execute_script("arguments[0].click();", element)

    def get_treasure_value(self):
        """Возвращает значение valuex у картинки-сундука."""
        treasure = self.find_element(self.TREASURE_IMG)
        return float(treasure.get_attribute("valuex"))

    def get_input_value(self):
        """Возвращает число из элемента input_value."""
        element = self.find_element(self.INPUT_VALUE)
        return int(element.text)

    def enter_answer(self, answer):
        """Вводит ответ в поле answer."""
        input_field = self.find_element(self.ANSWER_INPUT)
        input_field.send_keys(str(answer))

    def click_robot_checkbox(self):
        """Отмечает checkbox I'm the robot."""
        checkbox = self.find_element(self.ROBOT_CHECKBOX)
        checkbox.click()

    def click_robots_radio(self):
        """Выбирает radio Robots rule."""
        radio = self.find_element(self.ROBOTS_RADIO)
        self.scroll_to_element(radio)
        self.click_with_js(radio)

    def submit(self):
        """Нажимает кнопку Submit."""
        button = self.find_element(self.SUBMIT_BTN)
        self.scroll_to_element(button)
        self.click_with_js(button)

    def accept_alert(self):
        """Принимает alert и возвращает его текст."""
        alert = self.driver.switch_to.alert
        alert_text = alert.text
        alert.accept()
        return alert_text

    def get_num1(self):
        """Возвращает первое число."""
        element = self.find_element(self.NUM1)
        return int(element.text)

    def get_num2(self):
        """Возвращает второе число."""
        element = self.find_element(self.NUM2)
        return int(element.text)

    def get_sum(self):
        """Возвращает сумму двух чисел."""
        return self.get_num1() + self.get_num2()

    def select_sum_in_dropdown(self, sum_value):
        """Выбирает в dropdown опцию с переданным значением."""
        dropdown_element = self.find_element(self.DROPDOWN_SELECT)
        select = Select(dropdown_element)
        select.select_by_visible_text(str(sum_value))

    def fill_first_name(self, first_name):
        """Заполняет поле имени."""
        first_name_input = self.find_element(self.FIRST_NAME_INPUT)
        first_name_input.send_keys(first_name)

    def fill_last_name(self, last_name):
        """Заполняет поле фамилии."""
        last_name_input = self.find_element(self.LAST_NAME_INPUT)
        last_name_input.send_keys(last_name)

    def fill_email(self, email):
        """Заполняет поле email."""
        email_input = self.find_element(self.EMAIL_INPUT)
        email_input.send_keys(email)

    def upload_file(self, file_path):
        """Загружает файл в input type='file'."""
        file_input = self.find_element(self.FILE_INPUT)
        file_input.send_keys(str(file_path))

    def fill_registration_form(self, first_name, last_name, email, file_path):
        """Заполняет регистрационную форму с загрузкой файла."""
        self.fill_first_name(first_name)
        self.fill_last_name(last_name)
        self.fill_email(email)
        self.upload_file(file_path)
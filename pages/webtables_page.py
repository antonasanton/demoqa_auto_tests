import random

import allure
from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class WebtablesPage(BasePage):
    add_button = (By.ID, "addNewRecordButton")
    registration_form_title = (By.ID, "registration-form-modal")
    first_name = (By.ID, "firstName")
    last_name = (By.ID, "lastName")
    email = (By.ID, "userEmail")
    age = (By.ID, "age")
    salary = (By.ID, "salary")
    department = (By.ID, "department")
    submit_button = (By.ID, "submit")
    search = (By.XPATH, "//input[@placeholder='Type to search']")

    @allure.step("Ввод новых данных")
    def add_new_entry(self):
        name = f"name_{random.randint(0, 999999)}"
        last_name = f"name_{random.randint(0, 999999)}"
        email = "test@test.ru"
        age = 34
        salary = 3432
        department = "Gsjdhf"

        with allure.step("Нажатие кнопки 'Добавить'"):
            self.click(self.add_button)
        with allure.step("Поиск поля 'Регистрация'"):
            self.find_element(self.registration_form_title)
        with allure.step("Ввод имени"):
            self.enter_text(self.first_name, name)
        with allure.step("Ввод фамилии"):
            self.enter_text(self.last_name, last_name)
        with allure.step("Ввод email"):
            self.enter_text(self.email, email)
        with allure.step("Ввод возраста"):
            self.enter_text(self.age, age)
        with allure.step("Ввод дохода"):
            self.enter_text(self.salary, salary)
        with allure.step("Ввод департамента"):
            self.enter_text(self.department, department)
        with allure.step("Нажатие кнопки 'Submit"):
            self.click(self.submit_button)
        with allure.step("Поиск элемента с именем"):
            self.find_element((By.XPATH, f"//div[text()='{name}']"))

        return name

    @allure.step("Поиск данных")
    def find_entry(self, name):
        self.enter_text(self.search, name)
        self.find_element((By.XPATH, f"//div[text()='{name}']"))

    @allure.step("Очистка поисковой строки")
    def clear_search(self):
        element = self.find_element(self.search)
        element.clear()

    @allure.step("Редактирование введенных данных")
    def edit_entry(self, name):
        self.click((By.XPATH, f"//div[text()='{name}']/following-sibling::div[@role='gridcell']//span[@title='Edit']"))
        self.find_element(self.registration_form_title)
        name = f"name_{random.randint(0, 999999)}"
        self.enter_text(self.first_name, name)
        self.click(self.submit_button)
        self.find_element((By.XPATH, f"//div[text()='{name}']"))

        return name

    @allure.step("Удаление данных")
    def delete_entry(self, name):
        self.click((By.XPATH, f"//div[text()='{name}']/following-sibling::div[@role='gridcell']//span[@title='Delete']"))
        self.find_invisible_element((By.XPATH, f"//div[text()='{name}']"))

import allure
from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class TextBoxPage(BasePage):
    FULL_NAME = (By.ID, "userName")
    EMAIL = (By.ID, "userEmail")
    CURRENT_ADDRESS = (By.ID, "currentAddress")
    PERMANENT_ADDRESS = (By.ID, "permanentAddress")
    SUBMIT_BUTTON = (By.ID, "submit")

    @allure.step("Заполнение формы")
    def fill_form(self, name, email, current_address, permanent_address):
        self.enter_text(self.FULL_NAME, name)
        self.enter_text(self.EMAIL, email)
        self.enter_text(self.CURRENT_ADDRESS, current_address)
        self.enter_text(self.PERMANENT_ADDRESS, permanent_address)

    @allure.step("Нажатие кнопки Submit")
    def submit_form(self):
        self.click(self.SUBMIT_BUTTON)

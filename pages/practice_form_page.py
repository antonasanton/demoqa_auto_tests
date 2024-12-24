import os
from telnetlib import EC

import allure
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from pages.base_page import BasePage
from selenium.webdriver.common.keys import Keys

class PracticeFormPage(BasePage):
    name = (By.ID, "firstName")
    last_name = (By.ID, "lastName")
    email = (By.ID, "userEmail")
    gender = (By.XPATH, '//input[@name="gender"]/following-sibling::label')
    mobile = (By.ID, "userNumber")
    dob = (By.ID, "dateOfBirthInput")
    subjects = (By.ID, "subjectsInput")
    hobbies = (By.XPATH, '//label[contains(@for,"hobbies-checkbox")]')
    picture = (By.ID, "uploadPicture")
    address = (By.ID, "currentAddress")
    state = (By.ID, "react-select-3-input")
    city = (By.ID, "react-select-4-input")
    submit_button = (By.ID, "submit")

    @allure.step("Заполнение формы")
    def fill_form(self):
        name = "Yetti"
        last_name = "Collins"
        full_name = name + " " + last_name
        email = "2@3.com"
        mobile = 1234567890
        address = "234 skdfh"
        state = "NCR"
        city = "Delhi"
        state_city = state + " " + city
        picture = "beautiful-shot-white-british-shorthair-kitten.jpg"
        dob_month_list = (By.XPATH, "//select[@class='react-datepicker__month-select']/option")
        dob_year_list = (By.XPATH, "//select[@class='react-datepicker__year-select']/option")

        with allure.step("Заполнение поля 'Имя'"):
            self.enter_text(self.name, "Yetti")

        with allure.step("Заполнение поля 'Фамилия'"):
         self.enter_text(self.last_name, "Collins")

        with allure.step("Заполнение поля 'email'"):
            self.enter_text(self.email, "2@3.com")

        with allure.step("Рандомный выбор пола"):
            get_gender = self.get_random_element(self.gender)
            selected_gender = get_gender.text
            get_gender.click()

        with allure.step("Заполнение поля 'Mobile'"):
            self.enter_text(self.mobile, "1234567890")

        with allure.step("Заполнение поля 'Дата рождения'"):
            self.click(self.dob)
            self.click_random_element(dob_month_list)
            self.click_random_element(dob_year_list)


        with allure.step("Заполнение поля 'Subject'"):
            get_subjects = self.get_random_element(self.subjects)
            selected_subjects = get_subjects.text
            get_subjects.click()

        with allure.step("Заполнение поля 'Subject'"):
            self.send_keys(self.subjects, "NCR")
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.hobbies))

        with allure.step("Заполнение поля 'Hobbits'"):
            get_hobbies = self.get_random_element(self.hobbies)
            selected_hobbies = get_hobbies.text
            get_hobbies.click()

        path_to_picture = os.path.abspath("/Users/anton/Downloads/beautiful-shot-white-british-shorthair-kitten.jpg")
        self.send_keys(self.picture, path_to_picture)
        self.send_keys(self.address, "234 skdfh")
        self.send_keys(self.state, "NCR")
        self.send_keys(self.state, Keys.ENTER)
        self.send_keys(self.city, "Delhi")
        self.send_keys(self.city, Keys.ENTER)
        self.click(self.submit_button)

        assert full_name == self.get_text((By.XPATH, "//td[text()='Student Name']/following-sibling::td"))
        assert email == self.get_text((By.XPATH, "//td[text()='Student Email']/following-sibling::td"))
        assert str(mobile) == self.get_text((By.XPATH, "//td[text()='Mobile']/following-sibling::td"))
        assert address == self.get_text((By.XPATH, "//td[text()='Address']/following-sibling::td"))
        assert state_city == self.get_text((By.XPATH, "//td[text()='State and City']/following-sibling::td"))
        assert picture == self.get_text((By.XPATH, "//td[text()='Picture']/following-sibling::td"))
        assert selected_gender == self.get_text((By.XPATH, "//td[text()='Gender']/following-sibling::td"))
        assert selected_subjects == self.get_text((By.XPATH, "//td[text()='Subjects']/following-sibling::td"))
        assert selected_hobbies == self.get_text((By.XPATH, "//td[text()='Hobbies']/following-sibling::td"))
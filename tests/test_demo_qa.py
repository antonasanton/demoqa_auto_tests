import allure
import pytest
from selenium.webdriver.common.by import By
from pages.text_box_page import TextBoxPage
from pages.practice_form_page import PracticeFormPage
from pages.webtables_page import WebtablesPage

class TestDemoQa:

    @allure.title("Test TextBox")
    @pytest.mark.smoke
    def test_fill_form(self, browser):
        page = TextBoxPage(browser)
        page.open("https://demoqa.com/text-box")

        page.fill_form("Антон", "anton@example.com", "Улица, дом 1", "Улица, дом 2")
        page.submit_form()

        output_name = page.find_element((By.ID, "name")).text
        print(f"Результат: {output_name}")
        assert "Антон" in output_name

    @allure.title("Test Webtables")
    @pytest.mark.smoke
    def test_webtables_form(self, browser):
        page = WebtablesPage(browser)
        page.open("https://demoqa.com/webtables")
        name = page.add_new_entry()
        name = page.edit_entry(name)
        page.delete_entry(name)
        page.find_entry("Cierra")

    @allure.title("Test Forms")
    @pytest.mark.smoke
    def test_practice_form(self, browser):
        page = PracticeFormPage(browser)
        page.open("https://demoqa.com/automation-practice-form")
        page.fill_form()



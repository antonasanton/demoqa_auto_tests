import random
import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    def open(self, url):
        self.driver.get(url)

    def find_invisible_element(self, locator):
        return self.wait.until(EC.invisibility_of_element_located(locator))

    def find_element(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    def find_elements(self, locator):
        return self.wait.until(EC.presence_of_all_elements_located(locator))

    def click(self, locator):
        element = self.find_element(locator)
        element.click()
        self.get_screenshot()

    def enter_text(self, locator, text):
        element = self.find_element(locator)
        element.clear()
        element.send_keys(text)

    def get_random_element(self, locator):
        return random.choice(self.find_elements(locator))

    def click_random_element(self, locator):
        random.choice(self.find_elements(locator)).click()

    def get_text(self, locator):
        return self.find_element(locator).text

    def send_keys(self, locator, keys):
        element = self.find_element(locator)
        element.send_keys(keys)

    @allure.step("Сделать скриншот")
    def get_screenshot(self):
        allure.attach(
            name="Скриншот",
            body=self.driver.get_screenshot_as_png(),
            attachment_type=allure.attachment_type.PNG,
        )






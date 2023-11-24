from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys


class Page:

    def __init__(self, driver):
        self.driver = driver

    def find_element(self, locator, timeout=10):
        try:
            wait = WebDriverWait(self.driver, timeout)
            elements = wait.until(EC.presence_of_all_elements_located(locator))
            if len(elements) == 1:
                return elements[0]
            elif len(elements) > 1:
                return elements
            else:
                print(f"No elements found with locator {locator}")
                return None
        except NoSuchElementException as e:
            print(f"Element {locator} not found on the page: {e}")
            return None

    def click_element(self, locator, timeout=10):
        try:
            wait = WebDriverWait(self.driver, timeout)
            element = wait.until(EC.element_to_be_clickable(locator))
            element.click()
        except Exception as e:
            raise e

    def wait_for_element_and_send_keys(self, locator, keys, timeout=10):
        try:
            wait = WebDriverWait(self.driver, timeout)
            element = self.find_element(locator, timeout)
            element.click()

            actions = ActionChains(self.driver)
            actions.click(element).key_down(Keys.CONTROL).send_keys('a').key_up(Keys.CONTROL).send_keys(
                Keys.DELETE).perform()

            actions.send_keys(keys).perform()
        except Exception as e:
            raise e


import allure
import pytest
from decouple import config
from framework.login_page import LoginPage
from utils.logger_config import logger

log = logger()


@allure.feature("Authorization")
class TestUserLogin:
    LOGIN_CREDENTIAL = config('USER_CREDENTIAL')
    PASSWORD_CREDENTIAL = config('PASSWORD_CREDENTIAL')
    WRONG_LOGIN_CREDENTIAL = "wrong_email"
    WRONG_PASSWORD_CREDENTIAL = "wrong_password"

    @allure.description("Authorization tests")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.tag("smoke")
    @pytest.mark.parametrize("user_login, user_password, expected_elements", [
        (LOGIN_CREDENTIAL, PASSWORD_CREDENTIAL, [LoginPage.ADD_HUB_BUTTON, LoginPage.SIDE_BAR]),
        (WRONG_LOGIN_CREDENTIAL, WRONG_PASSWORD_CREDENTIAL,
         [LoginPage.EMAIL_FIELD, LoginPage.PASSWORD_FIELD, LoginPage.FORGOT_PASSWORD_BUTTON])
    ])
    def test_user_login(self, user_login_fixture, user_login, user_password, expected_elements):
        log.info("Starting test_user_login")

        login_page = LoginPage(user_login_fixture.driver)
        login_page.sign_in(user_login, user_password)

        try:
            login_page.assert_elements(expected_elements)
        except AssertionError as e:
            login_page.attach_screenshot_on_failure()
            log.error(f"AssertionError occurred: {e}")
            raise e

        if expected_elements == [LoginPage.ADD_HUB_BUTTON, LoginPage.SIDE_BAR]:
            login_page.log_out()
        elif expected_elements == [LoginPage.EMAIL_FIELD, LoginPage.PASSWORD_FIELD, LoginPage.FORGOT_PASSWORD_BUTTON]:
            login_page.click_element(login_page.BACK_BUTTON)

    @allure.description("Checking SideBar elements")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.tag("smoke")
    def test_check_sid_bar(self, user_login_fixture):
        log.info("Starting test_check_sid_bar")

        login_page = LoginPage(user_login_fixture.driver)
        login_page.sign_in(self.LOGIN_CREDENTIAL, self.PASSWORD_CREDENTIAL)
        login_page.click_element(login_page.SIDE_BAR)
        list_elements_with_icon = login_page.find_element(login_page.LIST_SID_BAR_ELEMENTS)

        elements_to_check = [
            login_page.ADD_HUB_BUTTON,
            login_page.SETTINGS_BUTTON,
            login_page.REPORT_ISSUE_BUTTON,
            login_page.CAMERA_BUTTON,
            login_page.HELP_BUTTON
        ]

        try:
            assert len(list_elements_with_icon) == 10
            login_page.assert_elements(elements_to_check)
        except AssertionError as e:
            login_page.attach_screenshot_on_failure()
            log.error(f"AssertionError occurred: {e}")
            raise e

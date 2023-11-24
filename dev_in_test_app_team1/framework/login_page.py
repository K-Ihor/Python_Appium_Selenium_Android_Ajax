import allure
from .page import Page
from selenium.webdriver.common.by import By


class LoginPage(Page):

    SIGN_IN_BUTTON = (By.ID, "com.ajaxsystems:id/authHelloLogin")
    LOG_IN_BUTTON = (By.ID, 'com.ajaxsystems:id/authLogin')
    EMAIL_FIELD = (By.ID, "com.ajaxsystems:id/authLoginEmail")
    PASSWORD_FIELD = (By.ID, "com.ajaxsystems:id/authLoginPassword")
    ADD_HUB_BUTTON = (By.ID, "com.ajaxsystems:id/hubAdd")
    SIDE_BAR = (By.ID, "com.ajaxsystems:id/menuDrawer")
    FORGOT_PASSWORD_BUTTON = (By.ID, "com.ajaxsystems:id/authLoginForgotPassword")
    SETTINGS_BUTTON = (By.ID, "com.ajaxsystems:id/settings")
    LOG_OUT_BUTTON = (By.ID, "com.ajaxsystems:id/accountInfoLogoutNavigate")
    BACK_BUTTON = (By.ID, "com.ajaxsystems:id/back")
    LIST_SID_BAR_ELEMENTS = (By.XPATH, "//android.widget.ScrollView//android.view.View")
    HELP_BUTTON = (By.ID, "com.ajaxsystems:id/help")
    CAMERA_BUTTON = (By.ID, "com.ajaxsystems:id/camera")
    REPORT_ISSUE_BUTTON = (By.ID, "com.ajaxsystems:id/logs")

    @allure.step("Sign In")
    def sign_in(self, user_login, user_password):
        self.click_element(self.SIGN_IN_BUTTON)
        self.wait_for_element_and_send_keys(self.EMAIL_FIELD, user_login)
        self.wait_for_element_and_send_keys(self.PASSWORD_FIELD, user_password)
        self.click_element(self.LOG_IN_BUTTON)

    @allure.step("Log out")
    def log_out(self):
        self.click_element(self.SIDE_BAR)
        self.click_element(self.SETTINGS_BUTTON)
        self.click_element(self.LOG_OUT_BUTTON)
        self.find_element(self.SIGN_IN_BUTTON)

    @allure.step("Assert_elements")
    def assert_elements(self, list_of_elements):
        for element_locator in list_of_elements:
            element = self.find_element(element_locator)
            assert element.is_displayed(), f"Element {element_locator} is not displayed"

    def attach_screenshot_on_failure(self):
        allure.attach(self.driver.get_screenshot_as_png(),
            name="Test Failed Screenshot",
            attachment_type=allure.attachment_type.PNG)

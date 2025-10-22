from selenium.webdriver.support.expected_conditions import WebDriverOrWebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver.BasePage import BasePage
from selenium.webdriver.common.by import By

class LoginPage(BasePage):
        def __init__(self, driver):
            super().__init__(driver)
            self.login_xpath = '//ul[@class="nav navbar-nav"]//a[@href="/login"]'
            self.email_xpath = '//input[@data-qa="login-email"]'
            self.password_xpath = '//input[@data-qa="login-password"]'
            self.login_button_xpath = '//button[@data-qa="login-button"]'
            self.error_xpath = '//*[@id="form"]/div/div/div[1]/div/form/p'

        def ingresar_al_login(self):
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, self.login_xpath))
            ).click()


        def ingresar_email(self, email):
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, self.email_xpath))
            ).send_keys(email)

        def ingresar_password(self, password):
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.NAME, "password"))
            ).send_keys(password)

        def click_login(self):
            self.click_element(self.login_button_xpath)

        def dashboard_visible(self, user_name):
            try:
                #dinamicamente concateno con el nombre de usuario
                dashboard_xpath = '//li[contains(., "Logged in as '+ user_name + '")]'''

                element = WebDriverWait(self.driver, 20).until(
                    EC.visibility_of_element_located((By.XPATH, dashboard_xpath))
                )
                return element.is_displayed()
            except:
                return False


        def validar_error(self,mensaje_Error):
            try:
                element = WebDriverWait(self.driver, 10).until(
                    EC.visibility_of_element_located((By.XPATH, self.error_xpath))
                )
                return mensaje_Error in element.text
            except:
                return False

        def validar_si_estamos_en_login(self):
            try:
                element = WebDriverWait(self.driver, 20).until(
                    EC.visibility_of_element_located((By.XPATH, self.login_xpath))
                )
                return element.is_displayed()
            except:
                return False

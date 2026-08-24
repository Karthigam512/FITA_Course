from selenium.webdriver.common.by import By


class LoginPage:

    def __init__(self, driver):
        self.driver = driver
        # Locators
        self.username_input = (By.ID, "email")
        self.password_input = (By.ID, "password")
        self.login_button = (By.CSS_SELECTOR, "#content > div.container.py-5.py-sm-7 > div > div.card.card-lg.mb-5.mt-6.mt-lg-0 > div > form > div.d-grid > button")

    def enter_username(self, username):
        self.driver.find_element(*self.username_input).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element(*self.password_input).send_keys(password)

    def click_login(self):
        self.driver.find_element(*self.login_button).click()

    def reload(self):
        self.driver.get("https://imeetify.com/login")

    def display_message(self, message_xpath):
        text_message = self.driver.find_element(By.XPATH, message_xpath).text
        print(text_message)

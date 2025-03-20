from Library import ConfigReader

class RegistrationClass:

    def __init__(self, obj):
        global driver
        driver = obj

    def enter_username(self, username):
        driver.find_element_by_name(ConfigReader.fetchElementLocators("Registration","username_name")).send_keys(username)

    def enter_password(self, password):
        driver.find_element_by_name(ConfigReader.fetchElementLocators("Registration", "password_name")).send_keys(password)

    def enter_email(self, email):
        driver.find_element_by_name(ConfigReader.fetchElementLocators("Registration", "email_name")).send_keys(email)


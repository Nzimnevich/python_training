from selenium.webdriver.common.by import By


class SessionHelper:
    def __init__(self, app):
        self.app = app

    def logout(self):
        wd = self.app.wd
        wd.find_element(By.LINK_TEXT, "Logout").click()

    def is_logged_in(self):
        wd = self.app.wd
        return len(wd.find_elements(By.LINK_TEXT, "Logout")) > 0

    def is_logged_in_as(self, user_name):
        wd = self.app.wd
        return wd.find_element(By.XPATH, "//*[@id='top']/form/b").text == "(" + user_name + ")"

    def ensure_logout(self):
        wd = self.app.wd
        if self.is_logged_in():
            self.logout()

    def login(self, user_name, password):
        wd = self.app.wd
        self.app.navigation.open_home_page()
        wd.find_element(By.NAME, "user").click()
        wd.find_element(By.NAME, "user").clear()
        wd.find_element(By.NAME, "user").send_keys(user_name)
        wd.find_element(By.ID, "LoginForm").click()
        wd.find_element(By.NAME, "pass").click()
        wd.find_element(By.NAME, "pass").clear()
        wd.find_element(By.NAME, "pass").send_keys(password)
        wd.find_element(By.XPATH, "//input[@value='Login']").click()

    def ensure_login(self, username, password):
        wd = self.app.wd
        if self.is_logged_in():
            if self.is_logged_in_as(username):
                return
            else:
                self.logout()
        self.login(self, username, password)

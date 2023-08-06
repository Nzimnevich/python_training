from selenium.webdriver.common.by import By


class GroupHelper:
    def __init__(self, app):
        self.app = app

    def create(self, group):
        wd = self.app.wd
        self.app.navigation.open_groups_page()
        # init group creation
        wd.find_element(By.XPATH, "//div[@id='content']/form/input[4]").click()
        # fill group form
        wd.find_element(By.NAME, "group_name").click()
        wd.find_element(By.NAME, "group_name").clear()
        wd.find_element(By.NAME, "group_name").send_keys(group.name)
        wd.find_element(By.NAME, "group_header").click()
        wd.find_element(By.NAME, "group_header").clear()
        wd.find_element(By.NAME, "group_header").send_keys(group.header)
        wd.find_element(By.NAME, "group_footer").click()
        wd.find_element(By.NAME, "group_footer").clear()
        wd.find_element(By.NAME, "group_footer").send_keys(group.footer)
        # submit group creation
        wd.find_element(By.NAME, "submit").click()
        self.app.navigation.open_groups_page()

    def click_enter_btn(self):
        wd = self.app.wd
        wd.find_element(By.XPATH, "//div[@id='content']/form/input[21]").click()

    def delete_first_group(self):
        wd = self.app.wd
        self.app.navigation.open_groups_page()
        # select first group
        wd.find_element(By.NAME, "selected[]").click()
        # submit deletion
        wd.find_element(By.NAME, "delete").click()
        self.app.navigation.open_groups_page()

    def changed_first_group(self, group):
        wd = self.app.wd
        self.app.navigation.open_groups_page()
        # select first group
        wd.find_element(By.XPATH, "//*[@class ='group']//input").click()
        self.click_edit_btn()
        # fill group form
        wd.find_element(By.NAME, "group_name").click()
        wd.find_element(By.NAME, "group_name").clear()
        wd.find_element(By.NAME, "group_name").send_keys(group.name)
        wd.find_element(By.NAME, "group_header").click()
        wd.find_element(By.NAME, "group_header").clear()
        wd.find_element(By.NAME, "group_header").send_keys(group.header)
        wd.find_element(By.NAME, "group_footer").click()
        wd.find_element(By.NAME, "group_footer").clear()
        wd.find_element(By.NAME, "group_footer").send_keys(group.footer)
        # submit group creation
        wd.find_element(By.NAME, "update").click()


    def click_edit_btn(self):
        wd = self.app.wd
        wd.find_element(By.NAME, "edit").click()
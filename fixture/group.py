from selenium.webdriver.common.by import By

from model.group import Group


class GroupHelper:
    def __init__(self, app):
        self.app = app

    def fill_group_form(self, group):
        self.change_field_value("group_name", group)
        self.change_field_value("group_header", group)
        self.change_field_value("group_footer", group)

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text.name is not None:
            wd.find_element(By.NAME, field_name).click()
            wd.find_element(By.NAME, field_name).clear()
            wd.find_element(By.NAME, field_name).send_keys(text.name)

    def create(self, group):
        wd = self.app.wd
        self.app.navigation.open_groups_page()
        # init group creation
        wd.find_element(By.XPATH, "//div[@id='content']/form/input[4]").click()
        # fill group form
        self.fill_group_form(group)
        # submit group creation
        wd.find_element(By.NAME, "submit").click()
        self.app.navigation.open_groups_page()
        self.group_cache = None

    def click_enter_btn(self):
        wd = self.app.wd
        wd.find_element(By.XPATH, "//div[@id='content']/form/input[21]").click()
        self.group_cache = None

    def delete_first_group(self):
        wd = self.app.wd
        self.app.navigation.open_groups_page()
        # select first group
        wd.find_element(By.NAME, "selected[]").click()
        # submit deletion
        wd.find_element(By.NAME, "delete").click()
        self.app.navigation.open_groups_page()
        self.group_cache = None

    def changed_first_group(self, new_group_data):
        wd = self.app.wd
        self.app.navigation.open_groups_page()
        # select first group
        self.select_first_group()
        self.click_edit_btn()
        # fill group form
        self.fill_group_form(new_group_data)
        # submit group creation
        wd.find_element(By.NAME, "update").click()

    def select_first_group(self):
        wd = self.app.wd
        wd.find_element(By.XPATH, "//*[@class ='group']//input").click()

    def click_edit_btn(self):
        wd = self.app.wd
        wd.find_element(By.NAME, "edit").click()
        self.group_cache = None

    def count(self):
        wd = self.app.wd
        self.app.navigation.open_groups_page()
        return len(wd.find_elements(By.NAME, "selected[]"))

    group_cache = None

    def get_groups(self):
        if self.group_cache is None:
            wd = self.app.wd
            self.app.navigation.open_groups_page()
            self.group_cache = []
            for element in wd.find_elements(By.CSS_SELECTOR, "span.group"):
                text = element.text
                id = element.find_element(By.NAME, "selected[]").get_attribute("value")
                self.group_cache.append(Group(name=text, id=id))

        return list(self.group_cache)

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from model.contact import Contact


class ContactHelper:
    def __init__(self, app):
        self.app = app

    def click_enter_btn(self):
        wd = self.app.wd
        wd.find_element(By.XPATH, "//div[@id='content']/form/input[21]").click()
        contact_cache = None

    def click_update_btn(self):
        wd = self.app.wd
        wd.find_element(By.NAME, "update").click()
        contact_cache = None

    def fill_add_contact_form(self, contact):
        wd = self.app.wd
        self.change_field_value("firstname", contact.firstname)
        self.change_field_value("middlename", contact.middlename)
        self.change_field_value("lastname", contact.lastname)
        self.change_field_value("title", contact.title)
        self.change_field_value("company", contact.company)
        self.change_field_value("address", contact.address)
        self.change_field_value("home", contact.home)
        self.change_field_value("mobile", contact.mobile)
        self.change_field_value("work", contact.work)
        self.change_field_value("fax", contact.fax)
        self.change_field_value("email", contact.email)
        self.change_field_value("email2", contact.email2)
        self.change_field_value("email3", contact.email3)
        self.change_field_value("homepage", contact.homepage)
        wd.find_element(By.NAME, "bday").click()
        Select(wd.find_element(By.NAME, "bday")).select_by_visible_text(contact.bday)
        wd.find_element(By.XPATH, "//option[@value='11']").click()
        wd.find_element(By.NAME, "bmonth").click()
        Select(wd.find_element(By.NAME, "bmonth")).select_by_visible_text(contact.bmonth)
        wd.find_element(By.XPATH, "//option[@value='February']").click()
        self.change_field_value("byear", contact.byear)
        wd.find_element(By.NAME, "aday").click()
        Select(wd.find_element(By.NAME, "aday")).select_by_visible_text(contact.aday)
        wd.find_element(By.XPATH, "//div[@id='content']/form/select[3]/option[17]").click()
        wd.find_element(By.NAME, "amonth").click()
        Select(wd.find_element(By.NAME, "amonth")).select_by_visible_text(contact.amonth)
        wd.find_element(By.XPATH, "//div[@id='content']/form/select[4]/option[12]").click()
        self.change_field_value("ayear", contact.ayear)
        self.change_field_value("address2", contact.address2)
        self.change_field_value("phone2", contact.phone2)
        self.change_field_value("notes", contact.notes)

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element(By.NAME, field_name).clear()
            wd.find_element(By.NAME, field_name).click()
            wd.find_element(By.NAME, field_name).clear()
            wd.find_element(By.NAME, field_name).send_keys(text)

    def delete_first_contact(self):
        self.delete_contact_by_index(0)

    def delete_contact_by_index(self, index):
        wd = self.app.wd
        # select first group
        wd.find_elements(By.XPATH, "//*[@name='entry']//input")[index].click()
        # click delete btn
        wd.find_element(By.XPATH, "//*[@id='content']/form[2]/div[2]/input").click()
        wd.switch_to.alert.accept()

    def changed_first_contact(self, contact):
        self.changed_contact_by_index(contact, 0)

    def changed_contact_by_index(self, contact, index):
        self.click_edite_btn(index)
        self.fill_add_contact_form(contact)

    def click_edite_btn(self, index):
        wd = self.app.wd
        ind = str(int(index) + 2)
        css_celector = f'tr:nth-child({ind}) > td:nth-child(8)'
        wd.find_element(By.CSS_SELECTOR, css_celector).click()

    def count(self):
        wd = self.app.wd
        self.app.navigation.open_add_contact_page()
        return len(wd.find_elements(By.NAME, "selected[]"))

    contact_cache = None

    def get_contacts(self):
        wd = self.app.wd
        self.contact_cache = []
        for element in wd.find_elements(By.CSS_SELECTOR, "[name='entry']"):
            lastname = element.find_element(By.CSS_SELECTOR, 'td:nth-child(2)').text
            firstname = element.find_element(By.CSS_SELECTOR, 'td:nth-child(3)').text
            id = element.find_element(By.CSS_SELECTOR, "input").get_attribute("value")
            self.contact_cache.append(Contact(lastname=lastname, firstname=firstname, id=id))
        return list(self.contact_cache)

# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from contact import Contact
import unittest


class UntitledTestCase(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.google.com/"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_add_contact_test_case(self):
        driver = self.driver
        self.open_login_page(driver)
        self.login(driver, "admin", "secret")
        self.open_add_contact_page(driver)
        self.fill_add_contact_form(driver, Contact("Nika", "Zimnevich", "sergeevna", "heloooo", "webinar", "drawertrtr street",
                                   "6", "792516728272", "33444", "we3333", "trtshjssj@gmail.ru",
                                   "trtshjss444j@gmail.ru", "trtshjssj3333@gmail.ru", "no", "11", "February", "1980",
                                   "15", "November", "2020", "djdjjd street", "34", "hi!"))
        self.click_enter_btn(driver)
        self.open_home_page(driver)
        self.logout(driver)

    def logout(self, driver):
        driver.find_element(By.LINK_TEXT, "Logout").click()

    def open_home_page(self, driver):
        driver.find_element(By.LINK_TEXT, "home page").click()

    def click_enter_btn(self, driver):
        driver.find_element(By.XPATH, "//div[@id='content']/form/input[21]").click()

    def fill_add_contact_form(self, driver, contact):
        driver.find_element(By.NAME, "firstname").click()
        driver.find_element(By.NAME, "firstname").clear()
        driver.find_element(By.NAME, "firstname").send_keys(contact.firstname)
        driver.find_element(By.NAME, "middlename").click()
        driver.find_element(By.NAME, "middlename").clear()
        driver.find_element(By.NAME, "middlename").send_keys(contact.middlename)
        driver.find_element(By.NAME, "lastname").click()
        driver.find_element(By.NAME, "lastname").clear()
        driver.find_element(By.NAME, "lastname").send_keys(contact.lastname)
        driver.find_element(By.NAME, "title").click()
        driver.find_element(By.NAME, "title").clear()
        driver.find_element(By.NAME, "title").send_keys(contact.title)
        driver.find_element(By.NAME, "company").click()
        driver.find_element(By.NAME, "company").clear()
        driver.find_element(By.NAME, "company").send_keys(contact.company)
        driver.find_element(By.NAME, "address").click()
        driver.find_element(By.NAME, "address").clear()
        driver.find_element(By.NAME, "address").send_keys(contact.address)
        driver.find_element(By.NAME, "home").click()
        driver.find_element(By.NAME, "home").clear()
        driver.find_element(By.NAME, "home").send_keys(contact.home)
        driver.find_element(By.NAME, "mobile").click()
        driver.find_element(By.NAME, "mobile").clear()
        driver.find_element(By.NAME, "mobile").send_keys(contact.mobile)
        driver.find_element(By.NAME, "work").click()
        driver.find_element(By.NAME, "fax").click()
        driver.find_element(By.NAME, "fax").clear()
        driver.find_element(By.NAME, "fax").send_keys(contact.fax)
        driver.find_element(By.NAME, "work").click()
        driver.find_element(By.NAME, "work").clear()
        driver.find_element(By.NAME, "work").send_keys(contact.work)
        driver.find_element(By.NAME, "email").click()
        driver.find_element(By.NAME, "email").click()
        driver.find_element(By.NAME, "email").clear()
        driver.find_element(By.NAME, "email").send_keys(contact.email)
        driver.find_element(By.NAME, "email2").click()
        driver.find_element(By.NAME, "email2").click()
        driver.find_element(By.NAME, "email2").clear()
        driver.find_element(By.NAME, "email2").send_keys(contact.email2)
        driver.find_element(By.NAME, "email3").click()
        driver.find_element(By.NAME, "email3").click()
        driver.find_element(By.NAME, "email3").clear()
        driver.find_element(By.NAME, "email3").send_keys(contact.email3)
        driver.find_element(By.NAME, "homepage").click()
        driver.find_element(By.NAME, "homepage").clear()
        driver.find_element(By.NAME, "homepage").send_keys(contact.homepage)
        driver.find_element(By.NAME, "bday").click()
        Select(driver.find_element(By.NAME, "bday")).select_by_visible_text(contact.bday)
        driver.find_element(By.XPATH, "//option[@value='11']").click()
        driver.find_element(By.NAME, "bmonth").click()
        Select(driver.find_element(By.NAME, "bmonth")).select_by_visible_text(contact.bmonth)
        driver.find_element(By.XPATH, "//option[@value='February']").click()
        driver.find_element(By.NAME, "byear").click()
        driver.find_element(By.NAME, "byear").clear()
        driver.find_element(By.NAME, "byear").send_keys(contact.byear)
        driver.find_element(By.NAME, "aday").click()
        Select(driver.find_element(By.NAME, "aday")).select_by_visible_text(contact.aday)
        driver.find_element(By.XPATH, "//div[@id='content']/form/select[3]/option[17]").click()
        driver.find_element(By.NAME, "amonth").click()
        Select(driver.find_element(By.NAME, "amonth")).select_by_visible_text(contact.amonth)
        driver.find_element(By.XPATH, "//div[@id='content']/form/select[4]/option[12]").click()
        driver.find_element(By.NAME, "ayear").click()
        driver.find_element(By.NAME, "ayear").clear()
        driver.find_element(By.NAME, "ayear").send_keys(contact.ayear)
        driver.find_element(By.NAME, "address2").click()
        driver.find_element(By.NAME, "address2").clear()
        driver.find_element(By.NAME, "address2").send_keys(contact.address2)
        driver.find_element(By.NAME, "phone2").click()
        driver.find_element(By.NAME, "phone2").clear()
        driver.find_element(By.NAME, "phone2").send_keys(contact.phone2)
        driver.find_element(By.NAME, "notes").click()
        driver.find_element(By.NAME, "notes").clear()
        driver.find_element(By.NAME, "notes").send_keys(contact.notes)

    def open_add_contact_page(self, driver):
        driver.find_element(By.LINK_TEXT, "add new").click()

    def login(self, driver, username, password):
        driver.find_element(By.NAME, "user").clear()
        driver.find_element(By.NAME, "user").send_keys(username)
        driver.find_element(By.NAME, "pass").click()
        driver.find_element(By.NAME, "pass").clear()
        driver.find_element(By.NAME, "pass").send_keys(password)
        driver.find_element(By.XPATH, "//input[@value='Login']").click()

    def open_login_page(self, driver):
        driver.get("http://localhost/addressbook/index.php")

    def is_element_present(self, how, what):
        try:
            self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e:
            return False
        return True

    def is_alert_present(self):
        try:
            self.driver.switch_to_alert()
        except NoAlertPresentException as e:
            return False
        return True

    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally:
            self.accept_next_alert = True

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)


if __name__ == "__main__":
    unittest.main()

# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_contact_test_case(app):
    app.navigation.open_add_contact_page()
    app.contact.fill_add_contact_form(
        Contact("Nika", "Zimnevich", "sergeevna", "heloooo", "webinar", "drawertrtr street",
                "6", "792516728272", "33444", "we3333", "trtshjssj@gmail.ru",
                "trtshjss444j@gmail.ru", "trtshjssj3333@gmail.ru", "no", "11", "February",
                "1980",
                "15", "November", "2020", "djdjjd street", "34", "hi!"))
    app.contact.click_enter_btn()
    app.navigation.open_home_page()

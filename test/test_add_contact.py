# -*- coding: utf-8 -*-
from model.contact import Contact
import pytest
from fixture.application import Application


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_contact_test_case(app):
    app.session.login(user_name="admin", password="secret")
    app.navigation.open_contact_page()
    app.contact.fill_add_contact_form(
        Contact("Nika", "Zimnevich", "sergeevna", "heloooo", "webinar", "drawertrtr street",
                "6", "792516728272", "33444", "we3333", "trtshjssj@gmail.ru",
                "trtshjss444j@gmail.ru", "trtshjssj3333@gmail.ru", "no", "11", "February",
                "1980",
                "15", "November", "2020", "djdjjd street", "34", "hi!"))
    app.contact.click_enter_btn()
    app.navigation.open_home_page()
    app.session.logout()

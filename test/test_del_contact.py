from model.contact import Contact


def test_delete_first_contact_test_case(app):
    if app.contact.count() == 0:
        app.navigation.open_add_contact_page()
        app.contact.fill_add_contact_form(Contact(firstname="group for deleting", bday="11", bmonth="February", aday="22", amonth="February", ayear="2020"))
        app.contact.click_enter_btn()
        app.navigation.open_home_page()
    app.contact.delete_first_contact()

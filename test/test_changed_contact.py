from model.contact import Contact
from random import randrange


def test_delete_some_contact_test_case(app):
    app.navigation.open_home_page()
    old_contacts = app.contact.get_contacts()
    index = randrange(len(old_contacts))
    if app.contact.count() == 0:
        app.navigation.open_add_contact_page()
        app.contact.fill_add_contact_form(Contact(firstname="group for deleting", bday="11", bmonth="February", aday="22", amonth="February", ayear="2020"))
        app.contact.click_enter_btn()
        app.navigation.open_home_page()

    contact = Contact("Cat", "Catt", "Kitten", "mya", "Cat factory", "meow-meow street",
                                              "6", "792516728272", "33444", "Cat factory", "nextlevel@gmail.ru",
                                              "nextlevel@gmail.ru", "nextlevel@gmail.ru", "no", "12", "November",
                                              "1990",
                                              "15", "February", "2020", "meow-meow street", "34", "meow!")
    contact.id = old_contacts[index].id

    app.contact.changed_contact_by_index(contact, index)
    app.contact.click_update_btn()
    app.navigation.open_home_page()
    new_contacts = app.contact.get_contacts()
    assert len(old_contacts) == len(new_contacts)
    old_contacts[index] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


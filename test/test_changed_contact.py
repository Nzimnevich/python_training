from model.contact import Contact


def test_delete_first_contact_test_case(app):
    app.session.login(user_name="admin", password="secret")
    app.contact.changed_first_contact(Contact("Cat", "Catt", "Kitten", "mya", "Cat factory", "meow-meow street",
                                              "6", "792516728272", "33444", "Cat factory", "nextlevel@gmail.ru",
                                              "nextlevel@gmail.ru", "nextlevel@gmail.ru", "no", "12", "November",
                                              "1990",
                                              "15", "February", "2020", "meow-meow street", "34", "meow!"))
    app.contact.click_enter_btn()
    app.session.logout()

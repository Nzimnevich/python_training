from model.group import Group


def test_add_group_test_case(app):
    app.session.login(user_name="admin", password="secret")
    app.group.changed_first_group(Group(name="cat", header="meo", footer="meow"))
    app.session.logout()

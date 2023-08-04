
def test_delete_first_group_test_case(app):
    app.session.login(user_name="admin", password="secret")
    app.group.delete_first_group()
    app.session.logout()

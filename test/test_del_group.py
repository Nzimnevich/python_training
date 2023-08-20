from model.group import Group


def test_delete_first_group_test_case(app):
    if app.group.count() == 0:
        app.group.create(Group(name="group for deleting"))
    app.group.delete_first_group()

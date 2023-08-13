from model.group import Group


def test_add_group_test_case(app):
    app.group.changed_first_group(Group(name="cat", header="meo", footer="meow"))


from model.group import Group


def test_changed_name_for_group_test_case(app):
    app.group.changed_first_group(Group(name="cat"))


def test_changed_header_for_group_test_case(app):
    app.group.changed_first_group(Group(header="meo"))

from model.group import Group


def test_delete_first_group_test_case(app):

    if app.group.count() == 0:
        app.group.create(Group(name="group for deleting"))
    old_groups = app.group.get_groups()
    app.group.delete_first_group()
    new_groups = app.group.get_groups()
    assert len(old_groups) - 1 == len(new_groups)
    old_groups[0:1] = []
    assert old_groups == new_groups

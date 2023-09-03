from model.group import Group
from random import randrange


def test_changed_name_for_group_test_case(app):
    if app.group.count() == 0:
        app.group.create(Group(name="group for changing"))
    old_groups = app.group.get_groups()
    index = randrange(len(old_groups))
    group = Group(name="cat")
    group.id = old_groups[index].id
    app.group.changed_group_by_index(index, group)
    new_groups = app.group.get_groups()
    assert len(old_groups) == len(new_groups)
    old_groups[index] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)

# def test_changed_header_for_group_test_case(app):
# if app.group.count() == 0:
#    app.group.create(Group(name="group for changing"))
# old_groups = app.group.get_groups()
# app.group.changed_first_group(Group(header="meo"))
# new_groups = app.group.get_groups()
# assert len(old_groups) == len(new_groups)

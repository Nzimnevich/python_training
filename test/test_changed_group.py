from model.group import Group


def test_changed_name_for_group_test_case(app):
    if app.group.count() == 0:
        app.group.create(Group(name="group for changing"))
    old_groups = app.group.get_groups()
    group = Group(name="cat")
    group.id = old_groups[0].id
    app.group.changed_first_group(group)
    new_groups = app.group.get_groups()
    assert len(old_groups) == len(new_groups)
    old_groups[0] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)


#def test_changed_header_for_group_test_case(app):
    #if app.group.count() == 0:
    #    app.group.create(Group(name="group for changing"))
    # old_groups = app.group.get_groups()
    # app.group.changed_first_group(Group(header="meo"))
    #new_groups = app.group.get_groups()
    #assert len(old_groups) == len(new_groups)
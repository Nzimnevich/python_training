# -*- coding: utf-8 -*-

from model.group import Group


def test_add_group_test_case(app):
    old_groups = app.group.get_groups()
    group = Group(name="ssdd", header="sssss", footer="sss")
    app.group.create(group)
    new_groups = app.group.get_groups()
    assert len(old_groups) + 1 == len(new_groups)
    old_groups.append(group)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)


def test_add_empty_group_test_case(app):
    old_groups = app.group.get_groups()
    group = Group(name="", header="", footer="")
    app.group.create(group)
    new_groups = app.group.get_groups()
    assert len(old_groups) + 1 == len(new_groups)
    old_groups.append(group)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)


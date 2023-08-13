# -*- coding: utf-8 -*-

from model.group import Group


def test_add_group_test_case(app):
    app.group.create(Group(name="ssdd", header="sssss", footer="sss"))


def test_add_empty_group_test_case(app):
    app.session.login(user_name="admin", password="secret")
    app.group.create(Group(name="", header="", footer=""))
    app.session.logout()

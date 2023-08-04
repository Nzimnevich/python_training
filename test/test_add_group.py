# -*- coding: utf-8 -*-

from model.group import Group
from fixture.application import Application
import pytest


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_group_test_case(app):
    app.login(user_name="admin", password="secret")
    app.create_group(Group(name="ssdd", header="sssss", footer="sss"))
    app.logout()


def test_add_empty_group_test_case(app):
    app.login(user_name="admin", password="secret")
    app.create_group(Group(name="", header="", footer=""))
    app.logout()

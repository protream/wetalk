# -*- coding: utf-8 -*-
"""
    wetalk.tests.test_front
    ~~~~~~~~~~~~~~~~~~~~~~~

    :copyright: (c) 2017 by protream.
"""


def test_home(app, client):
    rv = client.get('/')
    assert rv.status_code == 200

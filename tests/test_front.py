# -*- coding: utf-8 -*-
"""
    wetalk.tests.test_front
    ~~~~~~~~~~~~~~~~~~~~~~~

    :copyright: (c) 2017 by protream.
"""


def test_hello(app, client):
    rv = client.get(
        '/api/hello',
        headers={'content-type': 'application/json',
                 'accept': 'application/json'}
    )
    print(dir(rv))
    assert rv.status_code == 200
    assert rv.json == dict(message='Hello Vue!')

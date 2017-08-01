# -*- coding: utf-8 -*-
"""
    tests.conftest
    ~~~~~~~~~~~~~~

    :copyright: (c) 2017 by protream.
"""
import pytest
from wetalk.app import create_app


@pytest.fixture
def app():
    app = create_app('testing')
    return app


@pytest.fixture
def app_ctx(app):
    with app.app_context() as ctx:
        yield ctx


@pytest.fixture
def req_ctx(app):
    with app.test_app_context() as ctx:
        yield ctx


@pytest.fixture
def client(app):
    return app.test_client()

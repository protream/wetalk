# -*- coding: utf-8 -*-
"""
    wetalk.manage
    ~~~~~~~~~~~~~

    :copyright: (c) 2017 by protream.
"""
from wetalk import create_app


app = create_app('development')


@app.shell_context_processor
def make_shell_context():
    return {'a': 1}


if __name__ == '__main__':
    app.run()

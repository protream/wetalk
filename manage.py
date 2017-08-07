"""
    wetalk.manage
    ~~~~~~~~~~~~~

    :copyright: (c) 2017 by protream.
"""
import click
from colorama import Fore
from wetalk import db, create_app


app = create_app('development')


@app.shell_context_processor
def make_shell_context():
    d = {'db': db}
    d.update(dict(db.Model._decl_class_registry))
    return d


@app.cli.command('create_db',short_help='Drop existing tables and create database.')
def create_db_command():
    db.drop_all()
    db.create_all()
    click.echo('Database has benn created at ' +
               Fore.GREEN +
               app.config['SQLALCHEMY_DATABASE_URI'])


if __name__ == '__main__':
    app.run()

#! /usr/bin/env python

import os

from flask_script import Manager

from library_api import create_app, db

FLASK_ENV = os.getenv('LIBRARY_API_CONFIG', 'default')

app = create_app(FLASK_ENV)
manager = Manager(app)


@manager.shell
def make_shell_context():
    return dict(app=app, db=db)


if __name__ == '__main__':
    manager.run()

from flask import Flask, Response, make_response, request, render_template, redirect, url_for
from flask_migrate import Migrate,MigrateCommand
from flask_script import Manager

from apps.user.models import User
from apps import create_app
from ext import db

app = create_app()

manger = Manager(app=app)

Migrate(app=app, db=db)
manger.add_command('db',MigrateCommand)




@app.route('/', endpoint='index')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    manger.run()

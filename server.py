import os
from app import create_app, db
from flask.ext.script import Manager, Shell, Server
from flask.ext.migrate import Migrate, MigrateCommand

app = create_app(os.getenv('FLASK_CONFIG') or 'default')
manager = Manager(app)
manager.add_command("runserver", Server(host="0.0.0.0"))
migrate = Migrate(app, db)


def make_shell_context():
    return dict(app=app, db=db)
manager.add_command('shell', Shell(make_context=make_shell_context))
manager.add_command('db', MigrateCommand)


@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,PATCH')
    return response


@manager.command
def populate():
    from app.database import PopulateCountry, PopulateFake
    PopulateCountry.insert_countries()
    PopulateFake.insert_data()


@manager.command
def test():
    """Run the unit tests."""
    import unittest
    tests = unittest.TestLoader().discover('tests')
    successful = unittest.TextTestRunner(verbosity=2).run(tests).wasSuccessful()

    import sys
    sys.exit(successful is False)


if __name__ == '__main__':
    manager.run()

import os

from flask import Flask

def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'cashman.sqlite'),
    )

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    from . import db
    db.init_app(app)


    from .routes import transaction, income, expense
    app.register_blueprint(transaction.bp)
    app.register_blueprint(income.bp)
    app.register_blueprint(expense.bp)
    

    return app
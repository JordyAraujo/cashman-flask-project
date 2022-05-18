import os

from flask import Flask

from . import db
from .routes import expense, income, transaction


def create_app():
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY="dev",
        DATABASE=os.path.join(app.instance_path, "cashman.sqlite"),
    )

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    db.init_app(app)

    app.register_blueprint(transaction.bp)
    app.register_blueprint(income.bp)
    app.register_blueprint(expense.bp)

    return app

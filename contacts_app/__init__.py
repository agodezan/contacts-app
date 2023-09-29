""" some description """
# ----- Standard library ------
import os

# ----- Related third party ------
from dotenv import load_dotenv
from flask import Flask
from contacts_app.db.db import db_init


def create_app(app_name):
    """_summary_

    Args:
        app_name (_type_): _description_

    Returns:
        _type_: _description_
    """
    load_dotenv(".env")

    db_init()

    # if we need to import something from .env file
    conf_env = os.environ.get("FLASK_ENV", "development")

    print(conf_env)

    app = Flask(app_name)

    # initialize extensions
    # init_extensions(app)

    with app.app_context():
        # Import all the blueprints we will use.
        # Firstly the root blueprint and then all child blueprints
        # from root_bp import root_bp
        from contacts_app.home.routes import home_bp
        from contacts_app.contact.routes import contact_bp

        app.register_blueprint(home_bp)
        app.register_blueprint(contact_bp)

        # Finally register the root blueprint in the app
        # app.register_blueprint(root_bp)

    return app

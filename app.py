import logging
from flask import Flask
from views.auth_routes import auth_routes  # import auth routes
from views.drive_routes import drive_routes  # import drive routes
from importlib import import_module

def create_app(config_class="config.DevelopmentConfig"):
    app = Flask(__name__)
    app.config.from_object(config_class)

    # set up the logging
    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger(__name__)
    logger.info("Application starting...")

    # register both blueprints
    app.register_blueprint(auth_routes, url_prefix="/")
    app.register_blueprint(drive_routes, url_prefix="/drive")

    # log all of the routes
    for rule in app.url_map.iter_rules():
        logger.info(f"Route: {rule}, Endpoint: {rule.endpoint}")

    return app

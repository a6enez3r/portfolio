"""
    factory.py: contains function to configure & create flask web app
"""
import os
import logging

from flask import Flask, send_from_directory

from src.logs import SlackerLogHandler
from src.config import config_dict
from src.bps import register_blueprints
from src.extensions import secure_headers


def init_logs(app):
    """
    init global app logger
    """
    # logging
    # file
    logging.basicConfig(
        filename=app.config["LOGFILE"],
        level=app.config["LOGLEVEL"],
        format="%(name)-12s: [%(asctime)s] {%(pathname)s:%(lineno)d} %(levelname)s - %(message)s",
        datefmt="%H:%M:%S",
    )
    handlers = []
    # console
    console = logging.StreamHandler()
    console.setLevel(app.config["LOGLEVEL"])
    formatter = logging.Formatter(
        "%(name)-12s: [%(asctime)s] %(levelname)s - %(message)s"
    )
    console.setFormatter(formatter)
    handlers.append(console)
    # slack
    if app.config["SLACK_WEBHOOK_URL"]:
        slack = SlackerLogHandler(app.config["SLACK_WEBHOOK_URL"])
        slack.setLevel(logging.WARNING)
        formatter = logging.Formatter(
            "%(name)-12s: [%(asctime)s] {%(pathname)s:%(lineno)d} %(levelname)s - %(message)s",
        )
        slack.setFormatter(formatter)
        handlers.append(slack)
    # add all handlers
    for handler in handlers:
        logging.getLogger("").addHandler(handler)
        logging.getLogger("gunicorn.error").addHandler(handler)
        logging.getLogger("gunicorn.access").addHandler(handler)


def init_common(app):
    """
    init global app settings / routes
    """
    # favicon
    @app.route("/favicon.ico")
    def favicon():
        """
        render favicon
        """
        return send_from_directory(
            os.path.join(app.root_path, "static"),
            "favicon.ico",
            mimetype="image/vnd.microsoft.icon",
        )

    @app.after_request
    def set_secure_headers(response):
        secure_headers.framework.flask(response)
        return response


def create_app(environment="development"):
    """
    configure & create flask web application

    params:
        - environment: dev, prod or testing
    returns:
        - app: fully configured flask WSGI object
    """
    # create flask app
    app = Flask(__name__)
    # config
    app.config.from_object(config_dict[environment])
    # init
    init_logs(app)
    # shared
    init_common(app)
    # blueprints
    register_blueprints(app)
    # wsgi object
    return app

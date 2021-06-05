"""
    factory.py: contains function to configure & create flask web app
"""
# time
from time import strftime

# logging
import structlog

# flask
from flask import Flask, request

# config dict (contains dict of the format
# {"env_name": config_obj_for_env})
from src.config import config_dict

# config blueprints
from src.bps import register_blueprints

# extensions
from src.extensions import minimizer


logger = structlog.get_logger()


def create_logger(app):
    """
    create flask logger middleware
    """
    # for every request
    @app.after_request
    def after_request(response):  # pylint: disable=unused-variable
        # timestamp format
        timestamp = strftime("[%Y-%b-%d %H:%M]")
        # request information
        logger.info(
            "%s %s %s %s %s %s"
            % (
                timestamp,
                request.remote_addr,
                request.method,
                request.scheme,
                request.full_path,
                response.status,
            )
        )
        # return response
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
    # config here
    app.config.from_object(config_dict[environment])
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
    # config logger
    app.logger = logger
    # init minimizer
    minimizer.init_app(app)
    # init logger
    create_logger(app=app)
    # register blueprints
    register_blueprints(app)
    # return app
    return app

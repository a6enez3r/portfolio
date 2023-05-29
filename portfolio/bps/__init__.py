"""
    bps: contains all app blueprints + a single function to
                 iteratively register individual bps

    blueprints
        - pages - publicly accessible pages bp
        - errors - error handler pages bp
"""
import structlog
from flask import Flask

from portfolio.bps.errors import errors_bp
from portfolio.bps.pages import pages_bp

logger = structlog.get_logger()


def register_blueprints(app: Flask):
    """
    register blueprints to flask app

    Args
    ----
        - app (Flask): Flask app we are registering blueprints with
    """
    logger.debug("registering blueprints")
    logger.debug("register: errors")
    app.register_blueprint(errors_bp)
    logger.debug("register: pages")
    app.register_blueprint(pages_bp)

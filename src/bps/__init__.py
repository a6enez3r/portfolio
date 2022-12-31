"""
    __init__.py: contains all app blueprints + a single function to
                 iteratively register individual bps

    blueprints
        - pages - publicly accessible pages bp
        - errors - error handler pages bp
"""
# logging
import structlog

# error handlers
from src.bps.errors import errors_bp

# page handlers
from src.bps.pages import pages_bp

# init logger
logger = structlog.get_logger()


def register_blueprints(app):
    """
    register blueprints to flask app

    params:
        - app: Flask app we are registering blueprints with
    """
    # log
    logger.debug("registering blueprints")
    # register bps
    # log
    logger.debug("register: errors")
    # register
    app.register_blueprint(errors_bp)
    # log
    logger.debug("register: pages")
    # register
    app.register_blueprint(pages_bp)

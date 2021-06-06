"""
    errors.py: contains functions to render error pages
"""
# flask blueprint
from flask import Blueprint, render_template

errors_bp = Blueprint(
    "errors_bp", __name__, template_folder="templates", static_folder="static"
)


@errors_bp.app_errorhandler(400)
def bad_request(error):
    """
    bad request handler
    """
    # error code
    error_code = 400
    # return error page
    return (
        render_template("error.html", error_message=str(error), error_code=error_code),
        400,
    )


@errors_bp.app_errorhandler(404)
def not_found(error):
    """
    not found handler
    """
    # error code
    error_code = 404
    # return error page
    return (
        render_template("error.html", error_message=str(error), error_code=error_code),
        404,
    )


@errors_bp.app_errorhandler(405)
def forbidden(error):
    """
    forbidden request handler
    """
    # error code
    error_code = 405
    # return error page
    return (
        render_template("error.html", error_message=str(error), error_code=error_code),
        404,
    )


@errors_bp.app_errorhandler(500)
def server_error(error):
    """
    internal server error handler
    """
    # error code
    error_code = 500
    # return error page
    return (
        render_template("error.html", error_message=str(error), error_code=error_code),
        500,
    )


@errors_bp.app_errorhandler(502)
def bad_gateway(error):
    """
    bad gateway handler
    """
    # error code
    error_code = 502
    # return error page
    return (
        render_template("error.html", error_message=str(error), error_code=error_code),
        502,
    )

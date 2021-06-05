"""
    errors.py: contains functions to render error pages
"""
# flask blueprint
from flask import Blueprint, render_template

# minimizer
from src.extensions import minimizer
from flask_minify import decorators as minify_decorators

errors_bp = Blueprint(
    "errors_bp", __name__, template_folder="templates", static_folder="static"
)


@errors_bp.app_errorhandler(400)
@minify_decorators.minify(html=True, js=True, cssless=True)
def bad_request():
    """
    bad request handler
    """
    # error code
    status_code = 400
    # message
    message = "bad request."
    # return error page
    return (
        render_template("error.html", message=message, status_code=status_code),
        400,
    )


@errors_bp.app_errorhandler(404)
@minify_decorators.minify(html=True, js=True, cssless=True)
def not_found():
    """
    not found handler
    """
    # error code
    status_code = 404
    # message
    message = "resource not found."
    # return error page
    return (
        render_template("error.html", message=message, status_code=status_code),
        404,
    )


@errors_bp.app_errorhandler(405)
@minify_decorators.minify(html=True, js=True, cssless=True)
def forbidden():
    """
    forbidden request handler
    """
    # error code
    status_code = 405
    # message
    message = "resource forbidden."
    # return error page
    return (
        render_template("error.html", message=message, status_code=status_code),
        404,
    )


@errors_bp.app_errorhandler(500)
@minify_decorators.minify(html=True, js=True, cssless=True)
def server_error():
    """
    internal server error handler
    """
    # error code
    status_code = 500
    # message
    message = "internal server error."
    # return error page
    return (
        render_template("error.html", message=message, status_code=status_code),
        500,
    )


@errors_bp.app_errorhandler(502)
@minify_decorators.minify(html=True, js=True, cssless=True)
def bad_gateway():
    """
    bad gateway handler
    """
    # error code
    status_code = 502
    # message
    message = "bad gateway."
    # return error page
    return (
        render_template("error.html", message=message, status_code=status_code),
        502,
    )

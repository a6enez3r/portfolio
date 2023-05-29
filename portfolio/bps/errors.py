"""
    errors.py: contains functions to render error pages
"""
from flask import Blueprint, render_template
from flask_wtf.csrf import CSRFError

errors_bp = Blueprint(
    "errors",
    __name__,
    template_folder="templates",
    static_folder="static",
)


@errors_bp.app_errorhandler(400)
def bad_request(error):
    """
    Handle the HTTP 400 Bad Request error.

    Args
    ----
        - error: The error object representing the HTTP 400 error.

    Returns
    -------
        - The response to be sent back to the client.
    """
    status_code = 400
    return (
        render_template("error.html", message=str(error), status_code=status_code),
        400,
    )


@errors_bp.app_errorhandler(404)
def not_found(error):
    """
    Handle the HTTP 404 Not Found error.

    Args
    ----
        - error: The error object representing the HTTP 404 error.

    Returns
    -------
        - The response to be sent back to the client.
    """
    status_code = 404
    return (
        render_template("error.html", message=str(error), status_code=status_code),
        404,
    )


@errors_bp.app_errorhandler(405)
def forbidden(error):
    """
    Handle the HTTP 405 Forbidden error.

    Args
    ----
        - error: The error object representing the HTTP 405 error.

    Returns
    -------
        - The response to be sent back to the client.
    """
    status_code = 405
    return (
        render_template("error.html", message=str(error), status_code=status_code),
        404,
    )


@errors_bp.app_errorhandler(500)
def server_error(error):
    """
    Handle the HTTP 500 Internal Server error.

    Args
    ----
        - error: The error object representing the HTTP 500 error.

    Returns
    -------
        - The response to be sent back to the client.
    """
    status_code = 500
    return (
        render_template("error.html", message=str(error), status_code=status_code),
        500,
    )


@errors_bp.app_errorhandler(502)
def bad_gateway(error):
    """
    Handle the HTTP 502 Gateway Not Found error.

    Args
    ----
        - error: The error object representing the HTTP 502 error.

    Returns
    -------
        - The response to be sent back to the client.
    """
    # error code
    status_code = 502
    # return error page
    return (
        render_template("error.html", message=str(error), status_code=status_code),
        502,
    )


@errors_bp.app_errorhandler(CSRFError)
def handle_csrf_error(error):
    """
    Handle the HTTP CSRF error.

    Args
    ----
        - error: The error object representing the HTTP CSRF error.

    Returns
    -------
        - The response to be sent back to the client.
    """
    return (
        render_template("error.html", message=error.description, status_code=400),
        400,
    )

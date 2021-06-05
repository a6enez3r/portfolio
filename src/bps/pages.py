"""
    pages.py: contains functions to render pages
"""
# os
import os

# flask
from flask import Blueprint, render_template, send_from_directory, current_app

# data
from src.data import work_data, about_data, USER_NAME, social_links

pages_bp = Blueprint(
    "pages_bp", __name__, template_folder="templates", static_folder="static"
)


@pages_bp.route("/favicon.ico")
def favicon():
    """
    render favicon
    """
    return send_from_directory(
        os.path.join(current_app.root_path, "static"),
        "favicon.ico",
        mimetype="image/vnd.microsoft.icon",
    )


# work page
@pages_bp.route("/", methods=["GET"])
def work():
    """
    render work page
    """
    return (
        render_template(
            "work.html",
            USER_NAME=USER_NAME,
            work_data=work_data,
            social_links=social_links,
        ),
        200,
    )


# about page
@pages_bp.route("/about", methods=["GET"])
def about():
    """
    render about page
    """
    return (
        render_template(
            "about.html",
            USER_NAME=USER_NAME,
            about_data=about_data,
            social_links=social_links,
        ),
        200,
    )


# resume page
@pages_bp.route("/resume")
def resume():
    """
    render resume
    """
    # send resume file
    return send_from_directory(
        os.path.join(current_app.root_path, "static"), "resume.pdf"
    )

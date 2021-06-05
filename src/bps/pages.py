"""
    pages.py: contains functions to render pages
"""
# os
import os

# flask
from flask import Blueprint, render_template, send_from_directory, current_app

# minimizer
from flask_minify import decorators as minify_decorators

# data
from src.data import work_data, about_data, USER_NAME, social_links

pages_bp = Blueprint(
    "pages_bp", __name__, template_folder="templates", static_folder="static"
)

# work page
@pages_bp.route("/", methods=["GET"])
@minify_decorators.minify(html=True, js=True, cssless=True)
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
@minify_decorators.minify(html=True, js=True, cssless=True)
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
@minify_decorators.minify(html=True, js=True, cssless=True)
def resume():
    """
    render resume
    """
    # send resume file
    return send_from_directory(
        os.path.join(current_app.root_path, "static"), "resume.pdf"
    )

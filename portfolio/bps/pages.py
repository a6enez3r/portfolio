"""
    pages.py: contains functions to render pages
"""
import os

from flask import Blueprint, current_app, render_template, send_from_directory

from portfolio.gh import github_content
from portfolio.resume.parser import resume_content

pages_bp = Blueprint(
    "pages_bp", __name__, template_folder="templates", static_folder="static"
)


@pages_bp.route("/", methods=["GET"])
def experience():
    """
    Render the experience page.

    Returns
    -------
        - - The rendered HTML template as a string.
    """
    content = resume_content(
        os.path.join(current_app.root_path, "static", "resume/resume.html")
    )
    return (
        render_template(
            "experience.html",
            name=current_app.config["PORTFOLIO_USERNAME"],
            experiences=content["experiences"],
            links=content["links"],
        ),
        200,
    )


@pages_bp.route("/about", methods=["GET"])
def about():
    """
    Render the about page.

    Returns
    -------
        - - The rendered HTML template as a string.
    """
    content = resume_content(
        os.path.join(current_app.root_path, "static", "resume/resume.html")
    )
    projects = github_content(
        pat=current_app.config["GH_PAT"],
        username=current_app.config["GH_USERNAME"],
        saved=current_app.config["GH_FILE"],
    )
    return (
        render_template(
            "about.html",
            name=current_app.config["PORTFOLIO_USERNAME"],
            aboutme=content["aboutme"],
            projects=projects,
            links=content["links"],
        ),
        200,
    )


@pages_bp.route("/resume")
def resume():
    """
    Render the resume pdf.

    Returns
    -------
        - - The rendered HTML template as a string.
    """
    # send resume file
    return send_from_directory(
        os.path.join(current_app.root_path, "static"), "resume/resume.pdf"
    )

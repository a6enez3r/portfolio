"""
    pages.py: contains functions to render pages
"""
# os
import os

# flask
from flask import Blueprint, render_template, send_from_directory, current_app

# data
from src.data import experience, aboutme, links
from src.gh import github_projects

pages_bp = Blueprint(
    "pages_bp", __name__, template_folder="templates", static_folder="static"
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
            name=current_app.config["PORTFOLIO_USERNAME"],
            experience=experience,
            links=links,
        ),
        200,
    )


# about page
@pages_bp.route("/about", methods=["GET"])
def about():
    """
    render about page
    """
    projects = github_projects(
        pat=current_app.config["GH_PAT"], username=current_app.config["GH_USERNAME"]
    )
    return (
        render_template(
            "about.html",
            name=current_app.config["PORTFOLIO_USERNAME"],
            aboutme=aboutme,
            projects=projects,
            links=links,
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
        os.path.join(current_app.root_path, "static"), "resume/resume.pdf"
    )

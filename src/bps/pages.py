"""
    pages.py: contains functions to render pages
"""
# os
import os

# flask
from flask import Blueprint, current_app, render_template, send_from_directory

# data
from src.gh import github_content
from src.resume.parser import resume_content

pages_bp = Blueprint(
    "pages_bp", __name__, template_folder="templates", static_folder="static"
)

# experience page
@pages_bp.route("/", methods=["GET"])
def experience():
    """
    render work page
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


# about page
@pages_bp.route("/about", methods=["GET"])
def about():
    """
    render about page
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

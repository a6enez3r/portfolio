# flask dependencies
from flask import Flask, render_template, send_from_directory

# environment
from dotenv import load_dotenv

# logging
import logging

# config
import os

# import work
from portfolio.data import work_text, about_text

# load environment
load_dotenv()
# get environment
environment = os.environ.get("ENVIRONMENT")

# init app
app = Flask(__name__, static_url_path="/static")
# config
if environment == "production":
    # configure app
    app.config.from_object("config.ProductionConfig")
    # configure app logger
    logging.basicConfig(level=logging.ERROR)
else:
    # configure app
    app.config.from_object("config.DevelopmentConfig")
    # configure app logger
    logging.basicConfig(level=logging.DEBUG)

# work page
@app.route("/", methods=["GET"])
def work():
    # error handling
    try:
        return render_template("work.html", work_text=work_text), 200
    except Exception as e:
        # log
        app.logger.error("getting work page failed.")
        app.logger.error(str(e))
        # return error template
        return render_template("error.html"), 500


# about page
@app.route("/about", methods=["GET"])
def about():
    try:
        return render_template("about.html", about_text=about_text), 200
    except Exception as e:
        # log
        app.logger.error("getting work page failed.")
        app.logger.error(str(e))
        # return error template
        return render_template("error.html"), 500


# resume page
@app.route("/resume")
def resume():
    try:
        return send_from_directory(app.static_folder, filename="resume.pdf")
    except Exception as e:
        # log
        app.logger.error("getting work page failed.")
        app.logger.error(str(e))
        # return error template
        return render_template("error.html"), 500


# Generic error handling routes
@app.errorhandler(400)
def page_not_found(e):
    error_code = 400
    error_message = "bad request."
    return (
        render_template(
            "error.html", error_code=error_code, error_message=error_message
        ),
        400,
    )


@app.errorhandler(404)
def page_not_found(e):
    error_code = 404
    error_message = "page not found."
    return (
        render_template(
            "error.html", error_code=error_code, error_message=error_message
        ),
        404,
    )


@app.errorhandler(500)
def internal_server_error(e):
    error_code = 500
    error_message = "internal server errror."
    return (
        render_template(
            "error.html", error_code=error_code, error_message=error_message
        ),
        500,
    )


@app.errorhandler(502)
def internal_server_error(e):
    error_code = 502
    error_message = "bad gateway."
    return (
        render_template(
            "error.html", error_code=error_code, error_message=error_message
        ),
        502,
    )

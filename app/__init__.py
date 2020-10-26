import os
# flask dependencies
from flask import (
    Flask,
    render_template,
    send_from_directory,
    current_app
)

# environment manager
from dotenv import load_dotenv

# logging
import logging

# import data
from app.data import work_text, about_text, name
# config
import app.config as config
# load environment
load_dotenv()
# get environment
environment = os.environ.get("ENVIRONMENT")
# init app
app = Flask(__name__, static_url_path="/static")
# configure based on environment
if environment == "production":
    # configure app
    app.config.from_object(config.ProductionConfig)
else:
    # configure app
    app.config.from_object(config.DevelopmentConfig)
# import error handlers
from app.errors import errors as error_module
# register error handlers
app.register_blueprint(error_module)
# work page
@app.route("/", methods=["GET"])
def work():
    # error handling
    try:
        return render_template("work.html", name=name, work_text=work_text), 200
    except Exception as e:
        # log
        current_app.logger.error("getting work page failed.")
        current_app.logger.error(str(e))
        # return error template
        return render_template("error.html"), 500
# about page
@app.route("/about", methods=["GET"])
def about():
    try:
        return render_template("about.html", name=name, about_text=about_text), 200
    except Exception as e:
        # log
        current_app.logger.error("getting work page failed.")
        current_app.logger.error(str(e))
        # return error template
        return render_template("error.html"), 500
# resume page
@app.route("/resume")
def resume():
    try:
        # send resume file
        return send_from_directory(app.static_folder, filename="resume.pdf")
    except Exception as e:
        # log
        current_app.logger.error("getting work page failed.")
        current_app.logger.error(str(e))
        # return error template
        return render_template("error.html"), 500
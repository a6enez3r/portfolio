# flask dependencies
from flask import Flask, render_template, send_from_directory
# environment
from dotenv import load_dotenv
# logging
import logging
# config
import os
# import work
from portfolio.data import work_list
# load environment
load_dotenv()
# get environment
environment = os.environ.get("ENVIRONMENT")

# init app
app = Flask(__name__, static_url_path='/static')
# config
if environment == "production":
    # configure app
    app.config.from_object('config.ProductionConfig')
    # configure app logger
    logging.basicConfig(level=logging.ERROR)
else:
    # configure app
    app.config.from_object('config.DevelopmentConfig')
    # configure app logger
    logging.basicConfig(level=logging.DEBUG)
    
# work page
@app.route('/', methods=['GET'])
def work():
    # error handling
    try:
        # group work experience
        grouped_work_list = [work_list[i:i+2] for i in range(0, len(work_list), 2)]
        return render_template('work.html', grouped_work_list=grouped_work_list), 200
    except Exception as e:
        # log
        app.logger.error("getting work page failed.")
        app.logger.error(str(e))
        # return error template
        return render_template('error.html'), 500
# about page
@app.route('/about', methods=['GET'])
def about():
    try:
        return render_template('about.html'), 200
    except Exception as e:
        # log
        app.logger.error("getting work page failed.")
        app.logger.error(str(e))
        # return error template
        return render_template('error.html'), 500
# resume page
@app.route('/resume')
def resume():
    try:
        return send_from_directory(app.static_folder, filename="resume.pdf")
    except Exception as e:
        # log
        app.logger.error("getting work page failed.")
        app.logger.error(str(e))
        # return error template
        return render_template('error.html'), 500

# Routes for google analytics
@app.route('/google51951de21c061dc9.html', methods=['GET'])
def google_gsuite_verification():
    return render_template('google51951de21c061dc9.html')

@app.route('/google087c96628ea965db.html', methods=['GET'])
def google_webmaster_tools_verification():
    return render_template('google087c96628ea965db.html')

# Generic error handling routes
@app.errorhandler(404)
def page_not_found(e):
    error_code = 404
    error_message = "page not found."
    return render_template('error.html', error_code=error_code, error_message=error_message), 404

@app.errorhandler(500)
def internal_server_error(e):
    error_code = 500
    error_message = "internal server errror."
    return render_template('error.html', error_code=error_code, error_message=error_message), 500

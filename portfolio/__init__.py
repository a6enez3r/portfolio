# Import dependencies
from flask import Flask, render_template, request, flash, redirect, url_for, jsonify, send_from_directory, json
import config

# Initialise app
app = Flask(__name__, static_url_path='/static')
# Get configuration
app.config.from_object('config.ProductionConfig')


@app.route('/', methods=['GET'])
def work():
    # error handling
    try:
        return render_template('work.html'), 200
    except:
        return render_template('500.html'), 500

@app.route('/about', methods=['GET'])
def about():
    try:
        return render_template('about.html'), 200
    except Exception as e:
        return render_template('500.html'), 500

@app.route('/resume')
def resume():
    try:
        return send_from_directory(app.static_folder, filename="resume.pdf")
    except Exception as e:
        return render_template('500.html'), 500

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

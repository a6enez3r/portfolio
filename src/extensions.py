"""
    extensions.py: init flask extensions
"""
from flask_minify import minify

# init minify
minimizer = minify(passive=True)

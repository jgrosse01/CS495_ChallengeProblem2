"""
Author:         Jake Grosse
Created:        2/6/2022
Description:    Route for homepage of webapp
"""


# flask imports
from flask import Blueprint, render_template

# define this file as a blueprint for the main app
home = Blueprint('home', __name__)


# route home address
@home.route("/", methods=["GET"])
def select_search_type():
    return render_template('index.html')


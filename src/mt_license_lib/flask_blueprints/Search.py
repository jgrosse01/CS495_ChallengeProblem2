"""
Author:         Jake Grosse
Created:        2/6/2022
Description:    Route for search pages of webapp
"""

# flask imports
from flask import Blueprint, render_template

# define file blueprints
prefix_search = Blueprint('prefix_search', __name__)
city_search = Blueprint('city_search', __name__)


# route prefix search
@prefix_search.route("/search_by_prefix", methods=['GET'])
def search_by_prefix():
    return render_template("search_prefix.html")


# route county search
@city_search.route("/search_by_city", methods=['GET'])
def search_by_city():
    return render_template("search_city.html")

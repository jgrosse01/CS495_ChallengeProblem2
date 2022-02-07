"""
Author:         Jake Grosse
Created:        2/6/2022
Description:    A web-based app that satisfies the requirements of CS495 Challenge Problem 2
"""

# General Imports
from flask import Flask, redirect, render_template, request, url_for
from mt_license_lib.read_write.file_loader import read_csv, write_csv
import os

# flask blueprints
from mt_license_lib.flask_blueprints.Home import home
from mt_license_lib.flask_blueprints.Search import prefix_search, city_search
from mt_license_lib.flask_blueprints.Append import *
from mt_license_lib.flask_blueprints.Results import *
from mt_license_lib.flask_blueprints.Error import *
from mt_license_lib.flask_blueprints.EasterEgg import *

if __name__ == '__main__':
    # load in license list
    license_list = read_csv()

    # get path of template folder
    templates = os.path.abspath("../html_templates")

    # web app created with proper templates folder
    app = Flask(__name__, template_folder=templates)

    # register app blueprints to load pages and routes
    app.register_blueprint(home)
    app.register_blueprint(prefix_search)
    app.register_blueprint(city_search)

    # run app
    app.run(debug=True)

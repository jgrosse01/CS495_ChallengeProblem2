"""
Author:         Jake Grosse
Created:        2/6/2022
Description:    A web-based app that satisfies the requirements of CS495 Challenge Problem 2
"""

# General Imports
from flask import Flask
import os

# flask blueprints
from mt_license_lib.flask_blueprints.Home import home
from mt_license_lib.flask_blueprints.Search import prefix_search, city_search
from mt_license_lib.flask_blueprints.Results import prefix_result, city_result
from mt_license_lib.flask_blueprints.Append import append, append_entry
from mt_license_lib.flask_blueprints.Manual_Lookup import display_table

if __name__ == '__main__':
    # get path of template folder
    templates = os.path.abspath("../html_templates")

    # web app created with proper html_templates folder
    app = Flask(__name__, template_folder=templates)

    # register app blueprints to load pages and routes
    app.register_blueprint(home)
    app.register_blueprint(prefix_search)
    app.register_blueprint(city_search)
    app.register_blueprint(prefix_result)
    app.register_blueprint(city_result)
    app.register_blueprint(display_table)
    app.register_blueprint(append)
    app.register_blueprint(append_entry)

    # run app
    app.run(debug=True)

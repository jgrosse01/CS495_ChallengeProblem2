"""
Author:         Jake Grosse
Date Created:   8 February 2022
Description:    A blueprint that will serve to print the entire CSV.
"""
from flask import Blueprint, render_template
import pandas
import os

display_table = Blueprint('display', __name__)


@display_table.route("/manual_lookup", methods=['GET'])
def display(file_path=os.path.abspath('../data/MontanaCounties.csv')):
    df = pandas.read_csv(file_path)
    return render_template('table.html', tables=[df.to_html()], titles=[], title="Manual Database Lookup", search=False)

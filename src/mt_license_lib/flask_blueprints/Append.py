"""
Author:         Jake Grosse
Date Created:   15 February 2022
Description:    A method/blueprint used to validate and append a new city to the csv.
"""

from flask import Blueprint, request, render_template
from ..lookup.license_search import lookup_city
from ..read_write.file_loader import read_csv, write_csv
from ..util.text_manipulation import upper_fl
import re
# define blueprint
append = Blueprint('append_item', __name__)
append_entry = Blueprint('append_entry', __name__)

# some errors
invalid_code = "69420"
invalid_type = "INVALID APPEND INPUT"
invalid_hint = "You have entered a search term which is not valid for this search type. License Prefix is a number " \
               "and City is a word or phrase."


# method to append something to our file
@append.route("/append_item", methods=['POST'])
def append_item():
    data = read_csv()
    # make regex to search by
    regex_num = "[^\d]+"
    regex_alpha = "[^a-zA-Z\s]+"

    # get key from form and strip all non-valid characters
    prefix = re.sub(regex_num, "", request.form['prefix'])
    city = re.sub(regex_alpha, "", request.form['city_name'])
    county = re.sub(regex_alpha, "", request.form['county'])

    # if any are empty, their input is invalid so error pages
    if len(prefix) == 0:
        return render_template('error.html', term="add_entry", key=city, error_type=invalid_type + " PREFIX",
                               error_code=invalid_code, error_hint=invalid_hint)
    if len(city) == 0:
        return render_template('error.html', term="add_entry", key=city, error_type=invalid_type + " CITY",
                               error_code=invalid_code, error_hint=invalid_hint)
    if len(county) == 0:
        return render_template('error.html', term="add_entry", key=city, error_type=invalid_type + " COUNTY",
                               error_code=invalid_code, error_hint=invalid_hint)

    # if valid inputs, make sure the city does not exist
    found, entry = lookup_city(city, data)
    # if it exists, do not create two, error
    if found:
        return render_template('error.html', term="add_entry", key=city, error_type="Entry Already Exists",
                               error_code="2425", error_hint="Make sure you spell the entry correctly when searching.")

    write_csv(f"{upper_fl(county)},{upper_fl(city)},{prefix}\n")

    return render_template('appended.html')


# method to re-render append page
@append_entry.route("/append_entry_path/<key_val>", methods=['GET'])
def append_entry_method(key_val):
    return render_template('append_entry.html', key=key_val)

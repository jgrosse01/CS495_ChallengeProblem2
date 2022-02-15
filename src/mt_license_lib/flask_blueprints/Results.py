"""
Author:         Jake Grosse
Created:        12 February 2022
Description:    Blueprint to display the results of various search types.
"""
import pandas
import numpy as np
from flask import Blueprint, render_template, request, redirect, url_for
from ..read_write.file_loader import read_csv
from ..lookup.license_search import lookup_prefix, lookup_city
from ..util.text_manipulation import upper_fl
import re

# blueprints for rendering in webapp
prefix_result = Blueprint('prefix_results', __name__)
city_result = Blueprint('city_results', __name__)

# error type constants
invalid_code = "69420"
no_entry_code = "4269"
invalid_type = "INVALID SEARCH INPUT"
no_entry_type = "NO ENTRY UNDER SEARCH CRITERION"
invalid_hint = "You have entered a search term which is not valid for this search type. License Prefix is a number " \
               "and City is a word or phrase."
no_entry_hint = "There is not an entry for this search criterion in the data. Please search a different term."


# method to find results of a license prefix search
@prefix_result.route("/prefix_results", methods=['POST'])
def prefix_results():
    # read file
    data = read_csv()

    # make regex to search by
    regex = "[^\d]+"

    # get key from form and strip all non-valid characters
    key = re.sub(regex, "", request.form['prefix'])

    # after removing regex terms, if the term is invalid there will be nothing
    if key != "":
        # get result
        found, entries = lookup_prefix(int(key), data)
        if found:
            # if there is a result make a dataframe
            df = pandas.DataFrame(entries)
            # get the radio button from the form
            output = request.form['output']
            # if we only want county, drop the city
            if output == "county":
                df = df.drop('City', axis=1)
            # if we only want city, drop the county
            if output == "seat":
                df = df.drop('County', axis=1)
            if int(key) == 42:
                # easter egg :)
                return render_template('table.html', tables=[df.to_html()], titles=[], title="Prefix Search Results",
                                       search=True, term="prefix", val="easter")
            # return the end result html
            return render_template('table.html', tables=[df.to_html()], titles=[], title="Prefix Search Results",
                                   search=True, term="prefix")
        else:
            return render_template('error.html', error_code=no_entry_code, error_type=no_entry_type,
                                   error_hint=no_entry_hint, term="prefix")
    else:
        return render_template('error.html', error_code=invalid_code, error_type=invalid_type, error_hint=invalid_hint,
                               term="prefix")


# method to find results of a city search
@city_result.route("/city_results", methods=['POST'])
def city_results():
    # read file
    data = read_csv()

    # make regex to search by
    regex = "[^a-zA-Z\s]+"

    # get key from form
    key = re.sub(regex, "", request.form['city'])

    # after removing regex terms, if the term is invalid there will be nothing
    if key != "":
        found, entry = lookup_city(key, data)
        if found:
            # if there is an entry, put it in a dataframe because those are nice (and efficient)
            df = pandas.DataFrame(entry)
            # get the radio button output
            output = request.form['output']
            if output == "county":
                df = df.drop("City", axis=1)
            if output == "seat":
                df = df.drop("County", axis=1)
            # return the end result html
            return render_template('table.html', tables=[df.to_html()], titles=[], title="City Search Results",
                                   search=True, term="city")
        else:
            return redirect(url_for('append_entry.append_entry_method', key_val=key))
    else:
        return render_template('error.html', error_code=invalid_code, error_type=invalid_type, error_hint=invalid_hint,
                               term="city")

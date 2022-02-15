"""
Author:         Jake Grosse
Created:        6 February 2022
Description:    Lookup library for CS495 Challenge Problems.
"""


# function to look up given license prefix in a license list
def lookup_prefix(search_term: int, license_index: list) -> bool and dict:
    # for each entry in the list, search for the plate prefix passed in
    result = []
    for entry in license_index:
        if entry['License Plate Prefix'] == str(search_term):
            result.append(entry)
    # only return true and a result if there was at least one result found.
    if len(result) != 0:
        # compound return for whether the result was found and the result
        return True, result
    # if entry was not found to match, return False and None
    return False, None


# function to look up given county in a license list
def lookup_city(search_term: str, license_index: list) -> bool and dict:
    # for each entry in the list, search for the city passed in
    result = []
    for entry in license_index:
        if entry['City'].lower() == str(search_term).lower():
            result.append(entry)
    # only return true if there is something to return
    if len(result) != 0:
        # compound return for whether the result was found and the result
        return True, result
    # if entry was not found to match, return False and None
    return False, None

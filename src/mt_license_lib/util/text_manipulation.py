"""
Author:         Jake Grosse
Date Created:   14 February 2022
Description:    A text manipulation library to manipulate strings for ease of use.
"""


# a method to return a word with an uppercase first letter
def upper_fl(string: str) -> str:
    # make empty string
    ret_string = ""
    # split temp into a list of words separated by spaces
    temp = string.split()
    # make each word uppercase if it has a length greater than 1
    for item in temp:
        if len(item) > 1:
            # make sure to add a space at the end of the word, so it isn't all mashed together
            ret_string = ret_string + item[0:1].upper() + item[1:len(string)].lower() + " "
        else:
            # otherwise, just add the uppercase item and a space
            ret_string = ret_string + item.upper() + " "
    # return statement strips the last space off of the string
    return ret_string.strip()

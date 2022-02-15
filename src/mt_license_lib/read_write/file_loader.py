"""
Author:         Jake Grosse
Created:        6 February 2022
Description:    Read and write library for CS495 Challenge problems.
"""
import os


# function to read in data and return a structured list containing dictionary objects
def read_csv(filepath=os.path.abspath("../data/MontanaCounties.csv")):
    # list to return the loaded CSV file
    ret_list = []

    file = open(filepath)
    # read the first line of the file to get dictionary headers
    dict_headers = file.readline().strip('\n').split(',')

    # get all remaining lines
    lines = file.readlines()
    # close file
    file.close()

    # process lines and store in dictionary
    for line in lines:
        # split by commas for CSV file
        line = line.split(',')

        # temp dictionary to be appended to the list
        temp_dict = {}

        # append a line to the dictionary with its respective headers while stripping \n characters
        for i in range(len(dict_headers)):
            temp_dict[dict_headers[i]] = line[i].strip('\n')

        # append dictionary item to list, officially one line
        ret_list.append(temp_dict)

    # when all lines are loaded, return list
    return ret_list


# function to write data to the end of a specified file # WORKS, TESTED
def write_csv(line_to_write="", filepath=os.path.abspath("../data/MontanaCounties.csv")):
    # first open read file
    file = open(filepath, mode="r")
    # read all lines
    lines = file.readlines()
    # close read file
    file.close()

    # open write file
    file = open(filepath, mode='w')
    # add the line to be appended as lowercase
    lines.append(line_to_write)
    # write all lines to file
    file.writelines(lines)
    # close write file
    file.close()

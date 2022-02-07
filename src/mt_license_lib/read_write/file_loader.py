"""
Author:         Jake Grosse
Created:        6 February 2022
Description:    Read and write library for CS495 Challenge problems.
"""


# function to read in data and return a structured list containing dictionary objects
def read_csv(filepath="../data/MontanaCounties.csv"):
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
def write_csv(line_to_write="", filepath="../data/MontanaCounties.csv"):
    # first open file
    file = open(filepath, mode="rw")
    # read all lines
    lines = file.readlines()
    # add the line to be appended
    lines.append(line_to_write)
    # write all lines to file
    file.writelines(lines)
    # close file
    file.close()

    # the method below did not ensure consistent formatting

    # # first open file in read mode
    # file_read = open(filepath)
    # # get a list of the current lines
    # lines = file_read.readlines()
    # length = len(lines)
    # # close said file
    # file_read.close()
    #
    # # open the same file in append mode
    # file = open(filepath, mode='a')
    #
    # # append line given that there is an empty line at the end
    # # that is the format this was given, that is the format which will be maintained
    # # couldn't get it to properly work when trying to read if there was an empty line at the end of the document or not
    # file.write(f"{line_to_write}\n")
    #
    # # close the file when done
    # file.close()

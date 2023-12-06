#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    sort_dict = sorted(a_dictionary)
    for m in sort_dict:
        print("{}: {}".format(m, a_dictionary[m]))

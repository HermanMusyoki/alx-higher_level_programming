#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    dict_copy = a_dictionary.copy()
    for m, n in dict_copy.items():
        if value == n:
            a_dictionary.pop(m)
    return a_dictionary

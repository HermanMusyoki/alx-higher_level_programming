#!/usr/bin/python3
def search_replace(my_list, search, replace):
    return [replace if search == m else m for m in my_list]

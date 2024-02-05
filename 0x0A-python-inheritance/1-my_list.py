#!/usr/bin/python3
"""
Creates class inheriting from list class.
"""


class MyList(list):
    """Class MyList inherits."""

    def print_sorted(self):
        """Prints the list."""

        new_list = self[:]
        new_list.sort()
        print("{}".format(new_list))

#!/usr/bin/python3
""" MODULE """


class MyList(list):
    """ cls inherits from list
        prints sorted list
    """

    def print_sorted(self):
        print(sorted(self))

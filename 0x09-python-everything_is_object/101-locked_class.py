#!/usr/bin/python3
""" Locked Class """


class LockedClass:
    """ preventing new attr other than 'fn' """

    __slots__ = ('first_name')

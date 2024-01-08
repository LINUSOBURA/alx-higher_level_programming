#!/""""""usr/bin/python3
"""Simple lookup function"""


def lookup(obj):
    """functions returns a list of
    available attributes aand methods"""
    return list(dir(obj))

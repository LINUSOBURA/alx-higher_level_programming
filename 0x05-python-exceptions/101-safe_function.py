#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    try:
        fct(*args)
    except Exception as e:
        print("Exception: {}".format(str(e)), file=sys.stderr)
        return None

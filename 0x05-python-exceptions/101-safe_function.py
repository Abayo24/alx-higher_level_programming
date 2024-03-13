#!/usr/bin/python3
<<<<<<< HEAD
import sys


def safe_function(fct, *args):
    try:
        result = fct(*args)
        return result
    except Exception as e:
        print("Exception: {}".format(e), file=sys.stderr)
=======
def safe_function(fct, *args):
    try:
        r = fct(*args)
        return r
    except Exception as error:
        import sys
        print("Exception: {}".format(error), file=sys.stderr)
>>>>>>> master
        return None

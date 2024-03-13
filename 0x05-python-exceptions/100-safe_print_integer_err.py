#!/usr/bin/python3
<<<<<<< HEAD
import sys


def safe_print_integer_err(value):
    try:
        print("{:d}".format(value))
        return True
    except Exception as e:
        print(f"Exception: {e}", file=sys.stderr)
        return False
=======
def safe_print_integer_err(value):
    try:
        print("{:d}".format(value))
    except (ValueError, TypeError) as error:
        import sys
        print("Exception: {}".format(error), file=sys.stderr)
        return False
    else:
        return True
>>>>>>> master

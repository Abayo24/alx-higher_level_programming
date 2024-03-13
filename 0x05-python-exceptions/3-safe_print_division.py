#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        result = a / b
<<<<<<< HEAD
    except (ValueError, TypeError, ZeroDivisionError):
=======
    except ZeroDivisionError:
>>>>>>> master
        result = None
    finally:
        print("Inside result: {}".format(result))
    return result

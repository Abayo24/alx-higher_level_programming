#!/usr/bin/python3
<<<<<<< HEAD
if __name__ == "__main__":
    import sys
    total_arguments = len(sys.argv) - 1
    arguments = sys.argv
    if total_arguments == 0:
        print("{} arguments.".format(total_arguments))
    elif total_arguments == 1:
        print("{} argument:".format(total_arguments))
        for i, arg in enumerate(arguments[1:], start=1):
            print(f"{i}: {arg}")
    elif total_arguments > 1:
        print("{} arguments:".format(total_arguments))
        for i, arg in enumerate(arguments[1:], start=1):
            print(f"{i}: {arg}")
=======
if __name__ == '__main__':
    import sys
    if (len(sys.argv) - 1) != 1:
        print("{} arguments".format(len(sys.argv) - 1), end='')
    else:
        print("{} argument".format(len(sys.argv) - 1), end='')
    if len(sys.argv) == 1:
        print(".")
    else:
        print(":")
    for count, argument in enumerate(sys.argv):
        if (count == 0):
            continue
        print("{}: {}".format((count), argument))
>>>>>>> master

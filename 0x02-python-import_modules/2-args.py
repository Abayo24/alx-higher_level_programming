#!/usr/bin/python3
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

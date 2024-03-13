#!/usr/bin/python3
def no_c(my_string):
    new_string = ""
<<<<<<< HEAD
    for i in my_string:
        if i not in "Cc":
            new_string += i
=======
    for c in my_string:
        if c not in "Cc":
            new_string += c
>>>>>>> master
    return new_string

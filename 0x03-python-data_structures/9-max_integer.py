#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) == 0:
<<<<<<< HEAD
        return None
=======
        return ("None")
>>>>>>> master
    x = my_list[0]
    for i in my_list:
        if i > x:
            x = i
    return (x)

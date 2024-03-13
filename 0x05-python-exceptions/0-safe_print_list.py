#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
<<<<<<< HEAD
    n = 0
    for i in range(x):
        try:
            print(my_list[i], end="")
            n += 1
        except IndexError:
            break
    print()
    return n
=======
    c = 0
    for i in range(x):
        try:
            print(my_list[i], end="")
            c += 1
        except IndexError:
            break
    print()
    return c
>>>>>>> master

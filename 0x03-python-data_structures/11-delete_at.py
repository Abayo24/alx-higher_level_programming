#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
<<<<<<< HEAD
    new_list = []
    if idx <= 0 < len(my_list):
         del my_list[idx]
         return new_list
    else:
        return my_list
=======
    if 0 <= idx < len(my_list):
        del my_list[idx]
    return my_list
>>>>>>> master

#!/usr/bin/python3
def print_last_digit(number):
    if number < 0:
<<<<<<< HEAD
        last = -(number % -10)
    else:
        last = number % 10
    print(f"{last}", end='')
    return last
=======
        print("{:d}".format(-(number % -10)), end='')
        return(-(number % -10))
    else:
        print("{:d}".format(number % 10), end='')
        return(number % 10)
>>>>>>> master

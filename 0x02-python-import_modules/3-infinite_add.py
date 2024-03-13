#!/usr/bin/python3
<<<<<<< HEAD
if __name__ == "__main__":
    import sys
    summ = 0
    arguments = sys.argv[1:]
    for arg in arguments:
        summ += int(arg)
    print(f"{summ}")
=======
if __name__ == '__main__':
    import sys
    summation = 0
    argument_list = sys.argv[1:]
    for argument in argument_list:
        summation += int(argument)
    print("{}".format(summation))
>>>>>>> master

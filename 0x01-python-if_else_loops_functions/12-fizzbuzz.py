#!/usr/bin/python3
def fizzbuzz():
    for i in range(1, 101):
<<<<<<< HEAD
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz", end=' ')
        elif i % 3 == 0:
            print("Fizz", end=' ')
        elif i % 5 == 0:
            print("Buzz", end=' ')
        else:
            print("{:d}".format(i), end=' ')
=======
        if i % 3 == 0:
            print("Fizz", end='')
        if i % 5 == 0:
            print("Buzz", end='')
        if i % 3 and i % 5:
            print("{:d}".format(i), end='')
        print(end=' ')
>>>>>>> master

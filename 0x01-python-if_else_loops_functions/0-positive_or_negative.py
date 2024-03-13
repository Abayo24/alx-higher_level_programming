#!/usr/bin/python3
import random
number = random.randint(-10, 10)
<<<<<<< HEAD
if number < 0:
    print(f"{number} is negative")
elif number == 0:
    print(f"{number} is zero")
elif number > 0:
    print(f"{number} is positive")
=======
if number > 0:
    print(number, 'is positive')
elif number == 0:
    print(number, 'is zero')
else:
    print(number, 'is negative')
>>>>>>> master

#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
<<<<<<< HEAD
    result = list(map(lambda i: list(map(lambda x: x**2, i)), matrix))
    return result
=======
    return list(map(lambda submat: list(map(lambda e: e**2, submat)), matrix))    
>>>>>>> master

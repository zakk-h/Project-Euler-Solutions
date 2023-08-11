# How many possible routes are there in a 20x20 grid from the top left to bottom right corner when you can move either down or right, one unit at a time

import math

side_length = 20
exact_num_of_moves = side_length*2

def combination(n, k):
    #n choose k
    return math.factorial(n)//(math.factorial(k)*math.factorial(n-k))

#exact_num_of_moves choose side_length
#It is known that exactly 40 moves will be made, 20 down the y axis, and 20 going right on the x axis. The only thing which is not known is what order they come.
#In this case, k can be either x and y, but let a = n-k. n choose a = n choose k for any natural number a.
print(combination(exact_num_of_moves, side_length))
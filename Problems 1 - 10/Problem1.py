# -*- coding: utf-8 -*-
"""
Problem 1: Multiples of 3 and 5
https://projecteuler.net/problem=1

If we list all the natural numbers below 10 that are multiples of 3 or
5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
    
Find the sum of all the multiples of 3 or 5 below 1000.
"""
import timeit

# This problem can also be solved using arithmetic sums.
# We focus on a more code-centric solution here.

# This function returns a list of multiples of x, below n.
def multiples(x, n):
    multiple_list = []
    for i in range (1, -(-n//x)):  # Implement the ceiling function
        multiple_list.append(i*x)
    return multiple_list

# This prints the solution and the time to completion.
start = timeit.default_timer()
print(sum(list(set(multiples_below_n(3, 1000) + multiples_below_n(5,1000)))))
stop = timeit.default_timer()
print("Time:", stop - start)

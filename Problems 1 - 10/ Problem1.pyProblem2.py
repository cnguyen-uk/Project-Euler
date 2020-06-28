# -*- coding: utf-8 -*-
"""
Problem 2: Even Fibonacci numbers 
https://projecteuler.net/problem=2

Each new term in the Fibonacci sequence is generated by adding the
previous two terms. By starting with 1 and 2, the first 10 terms will
be:

1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

By considering the terms in the Fibonacci sequence whose values do not
exceed four million, find the sum of the even-valued terms.
"""
import timeit

# This function returns n Fibonacci terms, initialised with a and b.

def fib(a, b, n):
    fib_list = [a, b]
    for i in range(2, n):
        fib_list.append(fib_list[-1] + fib_list[-2])
    return fib_list

# This function returns Fibonacci terms up to a maximum limit L.
# We use the fact that F_L > L, so the iterable range is never reached.
# Note that in general this is not true, e.g. a = 0.1, b = 0.1.

def fib_up_to(a, b, L):
    for i in range(L):
        if fib(a, b, i)[-1] > L:
            return fib(a, b, i)[:-1]
        
# Prints the solution and ensures that it completes within 1 minute.

start = timeit.default_timer()
print(sum([i for i in fib_up_to(1, 2, 4000000) if i % 2 == 0]))
stop = timeit.default_timer()
print("Time:", stop - start)
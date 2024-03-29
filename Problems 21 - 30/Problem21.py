# -*- coding: utf-8 -*-
"""Problem 21: Amicable numbers

https://projecteuler.net/problem=21

Let d(n) be defined as the sum of proper divisors of n (numbers less
than n which divide evenly into n).
If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable
pair and each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22,
44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are
1, 2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.
"""
from custom_timer import computation_time


def d(n):
    """Return the value of d(n), as defined in the problem statement."""
    return sum([i for i in range(1, n) if not n % i])


def amicable_numbers(n):
    """Return a list of all amicable numbers under n."""
    return [i for i in range(1, n) if (i != d(i) and i == d(d(i)))]


@computation_time
def solution(n):
    """Return the solution, for all amicable numbers under n."""
    return sum(amicable_numbers(n))


print(solution(10000))

"""
Question 5
A positive integer n is said to be perfect if the sum of the factors of n, other than n itself, add up to n.
For instance 6 is perfect since the factors of 6 are {1,2,3,6} and 1+2+3=6.
Likewise, 28 is perfect because the factors of 28 are {1,2,4,7,14,28} and 1+2+4+7+14=28.

Write a Python function perfect(n) that takes a positive integer argument and returns True if the integer is perfect, and False otherwise.
"""

def perfect(n):
    sum = 0
    for i in range(1, n):
        if n % i == 0:
            sum += i
    return sum == n
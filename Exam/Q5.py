"""
Question 5
A positive integer n is a sum of three cubes if n = i3 + j3 + k3 for integers i,j,k such that i ≥ 1, j ≥ 1
and k ≥ 1. For instance, 10 is a sum of three cubes because 10 = 13 + 13 + 23, and so is 36 (13 + 23 + 33).
On the other hand, 4 and 11 are not sums of three cubes.

Write a Python function sum3cubes(n) that takes a positive integer argument and returns True if the integer is a sum of three cubes, and False otherwise.
"""

def sum3cubes(n):
  for i in range(n):
    for j in range(n):
      for k in range(n):
        if i ** 3 + j ** 3 + k ** 3 == n:
          return True
  return False
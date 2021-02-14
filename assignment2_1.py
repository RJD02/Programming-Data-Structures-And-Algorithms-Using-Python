"""
What do you want?
A function which takes an input m and returns True if m can be partitioned as primes
and False otherwise
# Question:

A positive integer m can be partitioned as primes if
it can be written as p + q where p > 0, q > 0 and both p and q are prime numbers.
Write a Python function primepartition(m) that takes an integer m as input and returns True if m can be partitioned
as primes and False otherwise. (If m is not positive, your function should return False.)
Example:
7 = 2 + 5 So True.
8 = 5 + 3 So True.
Sample Input:
>>> primepartition(7)
True

>>> primepartition(185)
False

>>> primepartition(3432)
True
"""

def seiveOfEratosthenes(n):
	prime = []
	for i in range(n + 1):
		prime.append(True)

	p = 2
	while(p * p <= n):
		if(prime[p]):
			for i in range(p * p, n + 1, p):
				prime[i] = False
		p = p + 1
	prime_list = []
	for p in range(n + 1):
		if prime[p]:
			prime_list.append(p)
	return prime_list

def check(prime_list, n):
	for i in prime_list:
		for j in prime_list:
			if i + j == n and i != 0 and j != 0:
				# print(i,j)
				return True
	return False

def primepartition(n):
	if n <= 0:
		return False
	prime_list = seiveOfEratosthenes(n)
	return check(prime_list, n)

n = int(input())
print(primepartition(n))
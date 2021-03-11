"""
Idea: Collect all the numbers which are divisible by 
Question: Should I fix first number to be taken always?
Answer: There could be a case where the longest Subsequence may consist of number starting not with first number but the second or third, etc..
        So we can't consider any number as fixed(not even the first one)

Let the input be a0, a1, a2...aN
So consider Best(i) to be the longest dividing sequence in a1, a2, a3...ai
Base condition: Best(1) = 1 i.e max(len(a0))

Case-1:
    If the next number is not divisible by the curr number then,
    Best(i + 1) = 1 + Best(i)
Case-2:
    If the next number is divisible by the curr number then,
    Best(i + 1) = 1 + max(Best(i + 2), Best(i + 3))
Or Best(i) = 1 + max(Best(
"""

def best(i, l):
    if i == 0:
        return 1
    max_count = 0
    for j in range(i):
        if l[i] % l[j] == 0:
            max_count = max(max_count, best(j, l) + 1)
    return max_count

def solve(l):
    max_count = 0
    for i in range(len(l)):
        max_count = max(max_count, best(i, l))
    return max_count

#  l = [2, 11, 16, 12, 36, 60, 71, 29, 144, 288, 129, 432, 993]
n = int(input())
l = []
for i in range(n):
    l.append(int(input()))
print(solve(l))

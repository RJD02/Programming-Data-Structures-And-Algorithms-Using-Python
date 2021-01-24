import time
def isArrayInSortedOrder(A):
    # base case
    if len(A) == 1:
        return True
    return A[0] <= A[1] and isArrayInSortedOrder(A[1:])

A = [127, 220, 246, 277, 321, 454, 534, 565, 934]
# print(isArrayInSortedOrder(A))
n = input()
n = int(n)
A = []
for i in range(1, n + 1):
    m = input()
    m = int(m)
    A.append(m)
print(isArrayInSortedOrder(A))

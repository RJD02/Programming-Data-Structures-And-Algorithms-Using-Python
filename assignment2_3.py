'''
What do you want?
I want a function which can rotate given list k times
and return a copy of the list

What is a rotation?
A  list rotation consists of taking the first element and moving it to the end.
For instance, if we rotate the list [1,2,3,4,5], we get [2,3,4,5,1].
If we rotate it again, we get [3,4,5,1,2].

So how does one rotation take place in code?
Given: l(list).
Let l = [1, 2, 3, 4, 5]
So rotated list looks like: l = [2, 3, 4, 5, 1]
so in code it must be:
l1 = l[1:]
l1 = l1 + l[0]
'''
"""
def rotatelist(l, k):
    if k < 0:
        return l
    l1 = l[:]
    l2 = []
    for i in range(0, k):
        l2 = l1[1:]
        l2 = l2.append(l1[i])
    return l2
"""

def rotatelist(l, k):
    if k < 0:
        return l
    k = k % len(l)
    l1 = l[k:] + l[:k]
    return l1

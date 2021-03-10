"""
Question 6
Write a Python function sublist(l1,l2) that takes two sorted lists as arguments and returns True if the the first list
 is a sublist of the second list, and returns False otherwise.

A sublist of a list is a segment consisting of contiguous values, without a gap. Thus, [2,3,4] is a sublist of [2,2,3,4,5], but [2,2,4] and [2,4,5] are not.
"""

def sublist(l1, l2):
    if len(l1) == 0:
        return False
    count = 0
    for i in l1:
        if i != l2[count]:
            return False
        count += 1
    return count == len(l1)

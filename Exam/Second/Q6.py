"""
Question 6
Write a Python function disjointlist(l1,l2) that takes two lists as arguments and returns True 
if the two lists are disjoint, otherwise returns False.

Two lists are said to be disjoint if there is no element that common to both the lists. 
For instance, [2,2,3,4,5] and [6,8,8,1] are disjoint, while [1,2,3,4] and [2,2] are not.
"""

def disjointlist(l1, l2):
  for i in l1:
    if i in l2:
      return False
  return True
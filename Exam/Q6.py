"""
Question 6
Write a Python function uncommon(l1,l2) that takes two lists sorted in ascending order as arguments
and returns the list of all elements that appear in exactly one of the two lists.
The list returned should be in ascending order. All such elements should be listed only once,
even if they appear multiple times in l1 or l2.

Thus, uncommon([2,2,4],[1,3,3,4,5]) should return [1,2,3,5] while uncommon([1,2,3],[1,1,2,3,3]) 
should return [].
"""

def uncommon(l1, l2):
  if len(l1) == 0:
    return l2
  if len(l2) == 0:
    return l1
  res = []
  for i in l2:
    if i not in res and i not in l1:
      res.append(i)
  for i in l1:
    if i not in l2 and i not in res:
      res.append(i)
  res.sort()
  return res
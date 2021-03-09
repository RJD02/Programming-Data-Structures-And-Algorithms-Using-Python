"""Question 4
A list is a decreasing if each element is strictly smaller than the preceding one.
For instance [], [7], [11,8] and [89,63,44,19,3] are decreasing, while [3,18,4] and [23,14,14,3]
are not. Here is a recursive function to check if a list is decreasing. 
You have to fill in the missing argument for the recursive call.

def decreasing(l):
  if l==[] or len(l) == 1:
    return(True)
  else:
    return(...)
"""

def decreasing(l):
  if l==[] or len(l) == 1:
    return(True)
  else:
    return(
       # Complete the recursive call below this line
l[0] > l[1] and decreasing(l[1:])
       # Complete the recursive call above this line
    )

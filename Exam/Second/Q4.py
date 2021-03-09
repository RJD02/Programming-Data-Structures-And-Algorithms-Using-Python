"""
Question 4
Recall that the positions in a list of length n are 0,1,…,n-1. We want to write a function 
mod3pos(l) that returns the elements at all positions in l that are divisible by 3. 
In other words, the function should return the list [l[0],l[3],...]. 
For instance mod3pos([]) == [], mod3pos([7]) == [7], mod3pos([8,11,8,11]) == [8,11] and 
mod3pos([19,3,44,44,3,19,17,23]) == [19,44,17]. A recursive definition of mod3pos is given below. 
You have to fill in the missing argument for the recursive call.

def mod3pos(l):
  if len(l) == 0:
    return([])
  else:
    return(...)
Open up the code submission box below and fill in the missing argument for the recursive call.
"""

def mod3pos(l):
  if len(l) == 0:
    return([])
  else:
    return(
       # Complete the recursive call below this line
       [l[i] for i in range(0, len(l), 3)]
    )
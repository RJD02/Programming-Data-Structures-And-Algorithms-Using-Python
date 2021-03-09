"""
Question 1
Here is an function to return the minimum value in a list. There is an error in this function. 
Provide an input list for which minbad produces an incorrect output.

def minbad(l):
  mymin = l[-len(l)]
  for i in range(-len(l),-1):
    if l[i] < mymin:
       mymin = l[i]
  return(mymin)
"""
[2, 1]
"""
# Question 1
Here is an function to return the maximum value in a list. There is an error in this function.
 Provide an input list for which maxbad produces an incorrect output.

def maxbad(l):
  mymax = l[-1]
  for i in range(-1,-len(l),-1):
    if l[i] > mymax:
       mymax = l[i]
  return(mymax)
Open up the code submission box below and 
write your test case where you would normally paste your code, below the line myinput = '''.
"""

[5, 3, 2, 1]
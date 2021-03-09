"""
Question 3
Here is a function to compute the third largest value in a list of distinct integers. All the integers 
are guaranteed to be positive. You have to fill in the missing lines. 
You can assume that there are at least three numbers in the list.

def thirdmax(l):
  (mymax,mysecondmax,mythirdmax) = (0,0,0)
  for i in range(len(l)):
  # Your code below this line


  # Your code above this line
  return(mythirdmax)
Open up the code submission box below and fill in the gap in the code. Ensure that you 
maintain correct indentation.
"""

def thirdmax(l):
  (mymax,mysecondmax,mythirdmax) = (0,0,0)
  for i in range(len(l)):
  	# You code below this line.
  	pass # He-he
  l.sort()
  return l[-3]
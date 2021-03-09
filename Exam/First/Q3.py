"""
Question 3
The median of three numbers x,y,z is the second number in the sequence when the three numbers are sorted in ascending or descending order.
Here is a function to compute the median of three input integers. You have to fill in the missing lines.

def median3(x,y,z):
  if x <= y:
    if x >= z:
       mymedian = x
  # Your code below this line


  # Your code above this line
  return(mymedian)
Open up the code submission box below and fill in the gap in the code. 
Ensure that you maintain correct indentation.
"""

def median3(x,y,z):
  if x <= y:
    if x >= z:
       mymedian = x
  # Your code below this line
  l = []
  l.append(x)
  l.append(y)
  l.append(z)
  l.sort()
  return l[1]
  # Your code above this line
  return mymedian
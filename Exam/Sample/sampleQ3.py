"""
Question 3
Here is a function to compute the largest of four input integers. You have to fill in the missing lines.

Code:

def max4(w,x,y,z):
  if w >= x and w >= y and w >= z:
    maximum = w
  # Your code below this line


  # Your code above this line
  return(maximum)
"""
def max4(w,x,y,z):
  if w >= x and w >= y and w >= z:
    maximum = w
  # Your code below this line
  elif x >= w and x >= y and x >= z:
      maximum = x
  elif y >= w and y >= x and y >= z:
      maximum = y
  else:
      maximum = z
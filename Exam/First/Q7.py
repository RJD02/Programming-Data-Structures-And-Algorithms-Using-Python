"""
Question 7
Write a Python program that reads input from the keyboard (standard input). The input will be
terminated by a blank line. The lines are numbered 0,1,2,… Your program should print out the 
even numbered lines followed by the odd numbered lines. In other words, first print lines 0,2,4,… 
then lines 1,3,5,…
"""

line = input()
print(line)
store = []
count = 1
line = input()
while line:
  if count % 2 == 0:
    print(line)
  else:
    store.append(line)
  count += 1
  line = input()
for i in store:
  print(i)
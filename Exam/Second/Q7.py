"""
Question 7
Write a Python program that reads input from the keyboard (standard input). The input will consist of an 
even number of lines of text. The input will be terminated by a blank line. Suppose there are 2n lines of 
input. Your program should print out the last n lines of the input, i.e., the second half of the input, 
followed by the first n lines, i.e., the first half of the input.

For instance, if the input is the following:

our dear friend,
let's eat

then the output should be:

let's eat
our dear friend,
"""

line = input()
store = []
while line:
	try:
		store.append(line)
		line = input()
	except:
		break
# print(store)
first_half = store[:len(store) // 2]
second_half = store[len(store) // 2:]
# print(first_half, second_half)
for i in second_half:
	print(i)
for i in first_half:
	print(i)
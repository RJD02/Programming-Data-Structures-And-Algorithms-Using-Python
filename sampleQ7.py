"""
Question 7
Write a Python program that reads input from the keyboard (standard input). The input will consist of some number of lines of text.
The input will be terminated by a blank line.
Your program should print every third line.

For instance, if the input is the following:

"Spot the mistake
in the following argument",
Jack challenged
1+(-1+1)+(-1+1)+... = (1+ -1)+(1+ -1)+...
so therefore,
1 = 0
??

then the output should be:

Jack challenged
1 = 0
"""

def sovle():
    count = 1
    line = input()
    while line:
        if count % 3 == 0:
            print(line)
            count += 1
        line = input()
    return

solve()
'''
# QUESTION:
Write a Python function splitsum(l) that takes a nonempty list of integers and
returns a list [pos,neg], where pos is the sum of squares all the positive numbers in l and
neg is the sum of cubes of all the negative numbers in l.

What do you want?
A separator function which can give me two list namely positive and negative.
Some function that could calculate sum of the provided list.
'''

def squareIt(l):
    sum = 0
    for i in l:
        sum += i * i
    return sum

def cubeIt(l):
    sum = 0
    for i in l:
        sum += i * i * i
    return sum

def splitsum(l):
    pos, neg = [], []
    for i in l:
        if i > 0:
            pos.append(i)
        elif i < 0:
            neg.append(i)
    positive_sum = squareIt(pos)
    negative_sum = cubeIt(neg)
    return [positive_sum, negative_sum]

print(splitsum([1,3,-5]))
print(splitsum([2,4,6]))
print(splitsum([-19,-7,-6,0]))
print(splitsum([-1,2,3,-7]))

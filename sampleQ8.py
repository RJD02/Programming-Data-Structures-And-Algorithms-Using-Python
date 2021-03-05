"""
Question 8
Write a Python function repeated(l) that takes a list of immutable values as argument.
The function should return the number of values that are repeated in the input list.

For instance, repeated([1,17,22,17,23,17]) should return 1 because only 1 value, 17 is repeated.
Likewise repeated(["the","higher","you","climb","the","further","you","fall"]) is 2 becaues 2 values, "the" and "you", are repeated.
"""

def repeated(l):
    count = 0
    for i in l:
        if l.count(i) > 1:
            count += 1
            for j in range(l.count(i)):
                l.remove(i)
    return count

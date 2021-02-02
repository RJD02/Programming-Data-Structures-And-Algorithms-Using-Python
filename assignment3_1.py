'''
Define a Python function remdup(l) that takes a nonempty list of integers l and
removes all duplicates in l, keeping only the last occurrence of each number.

What do you want?
I want a function which can remove the first occurrence of the given value from the list

This can be done by list1.remove().

So reversing the list makes it easier to use l.remove() function.
Algorithm:
1) Find repeated elements. And make it into a list.
2) Reverse the list.
3) Apply l.remove() function with the value from the repeated list obtained in step-1.
4) Return reversed list.
Ex:
Original list: 3, 1, 3, 5
Applying Algorithm-
1) repeated = [3]
2) l1 = [5,3,1,3]
3) l1.remove(3)
The list becomes: 5,1,3
4) Reversing:
The list becomes: 3,1,5

Somehow, the sample case and the test cases don't match.
I get what test cases are asking for:
They want the list with first duplicate removed!
Exactly opposite to what the question has asked!!! Gotta report their ass!!
'''

def which(l):
    l1 = l[:]
    l1.sort()
    repeated = []
    for i in range(len(l1) - 1):
        if l1[i] == l1[i + 1]:
            repeated.append(l1[i])
    return repeated

def remdup(l):
    repeated = which(l)
    for i in repeated:
        l.remove(i)
    return l

print(remdup([3, 1, 3, 5]))
print(remdup([7,3,-1,-5]))
print(remdup([3,5,7,5,3,7,10]))

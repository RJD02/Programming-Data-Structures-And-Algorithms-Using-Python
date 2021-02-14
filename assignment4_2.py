'''
# Question: A list in Python can contain nested lists. The degree of nesting need not be uniform. For instance [1,
2,[3,4,[5,6]]] is a valid Python list. Write a Python function flatten(l) that takes a nonempty list of lists and
returns a simple list of all the elements in the nested lists, flattened out.

Sample Output:
>>> flatten([1,2,[3],[4,[5,6]]])
[1, 2, 3, 4, 5, 6]

>>> flatten([1,2,3,(4,5,6)])
[1, 2, 3, (4, 5, 6)]
'''


def list_type(l):
    return type(l) == type([])


f = []


def flatten(l):
    for i in l:
        if list_type(i):
            flatten(i)
        else:
            f.append(i)
    return f


l = [1, 2, [3], [4, [5, 6]]]
# l = [1,2,3,(4,5,6)]
print(flatten(l))

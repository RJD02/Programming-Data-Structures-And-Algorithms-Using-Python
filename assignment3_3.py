'''
What do you want?
I want a function which takes a matrix as input and a character 'h' or 'v'.
Then flips(reverses) the rows or columns of the list.

How to flip rows?
1  2  3
4  5  6
7  8  9
is represented by [[1, 2, 3], [4, 5, 6], [7, 8, 9]].
So when we do row flip it should be like
3  2  1
6  5  4
9  8  7
which is represented by [[3, 2, 1], [6, 5, 4], [9, 8, 7]].
That is we have to reverse individual list elements.(inner)

How to flip columns?
3  2  1
6  5  4
9  8  7
is represented by [[3, 2, 1], [6, 5, 4], [9, 8, 7]].
So when we do column flip it should be like
9 8 7
6 5 4
3 2 1
which is represented by [[9, 8, 7], [6, 5, 4], [3, 2, 1]].
That is we have reverse the whole list itself.(outer)

Ex:
matrixflip([[1,2],[3,4], 'h')
[[2, 1], [4, 3]]
'''

def flipHorizontal(l):
    # l1 = l[:]
    for i in range(len(l)):
        l[i].reverse()
    return l

def flipVertical(l):
    # l1 = l[:]
    l.reverse()
    return l

def matrixflip(l, ch):
    l1 = l.copy()
    if ch == 'h':
        return flipHorizontal(l1)
    else:
        return flipVertical(l1)

print(matrixflip([[1,2],[3,4]], 'h'))
print(matrixflip([[1,2],[3,4]], 'v'))
print(matrixflip([[1, 2], [3, 4]],'h'))
# print(matrixflip(matrixflip([[1,2],[3,4]], 'h'), 'v'))

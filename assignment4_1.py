'''
We have a list of annual rainfall recordings of cities. Each element in the list is of the form (c,r)
where c is the city
and r is the annual rainfall for a particular year.
The list may have multiple entries for the same city, corresponding to rainfall recordings in different years.

Write a Python function rainaverage(l) that takes as input a list of rainfall recordings and
computes the avarage rainfall for each city.
The output should be a list of pairs (c,ar) where c is the city and ar is the average rainfall for this city among the
recordings in the input list.
Note that ar should be of type float. The output should be sorted in dictionary order with respect to the city name.

Here are some examples to show how rainaverage(l) should work.

>>> rainaverage([(1,2),(1,3),(2,3),(1,1),(3,8)])
[(1, 2.0), (2, 3.0), (3, 8.0)]

>>> rainaverage([('Bombay',848),('Madras',103),('Bombay',923),('Bangalore',201),('Madras',128)])
[('Bangalore', 201.0), ('Bombay', 885.5), ('Madras', 115.5)]
'''


def rainaverage(l):
    l.sort()
    d = {}
    count = {}
    for i in l:
        d[i[0]] = 0
        count[i[0]] = 1
    # print(l)
    for i in range(0, len(l) - 1):
        if l[i][0] == l[i + 1][0]:
            count[l[i][0]] += 1
    # print(count)
    for tup in l:
        d[tup[0]] += tup[1]
    # print(d)
    for i in d.keys():
        d[i] = d[i] / count[i]
    # print(d)
    res = []
    for i in d:
        tup = (i, d[i])
        res.append(tup)
    return res


print(rainaverage([(1, 2), (1, 3), (2, 3), (1, 1), (3, 8)]))
print(rainaverage([('Bombay', 848), ('Madras', 103), ('Bombay', 923), ('Bangalore', 201), ('Madras', 128)]))

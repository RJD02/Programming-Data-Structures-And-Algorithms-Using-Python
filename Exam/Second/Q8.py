"""
Question 8
Write a Python function maxdifference(l) that takes a list of pairs of the form (name,score) as argument, 
where name is a string and score is an integer. Each pair is to be interpreted as the score of the named player. 
For instance, an input of the form [('Kohli',73),('Ashwin',33),('Kohli',7),('Pujara',122),('Kohli',66),('Ashwin',90)] 
represents three scores of 73, 66 and 7 for Kohli, two scores of 33 and 90 for Ashwin and one score of 122 
for Pujara. Your function should compute the difference between the maximum and minimum score for each player 
and return the list of players for whom this difference is maximum. The list should be sorted in ascending 
order by the name of the player.

For instance, maxdifference([('Kohli',73),('Ashwin',33),('Kohli',7),('Pujara',122),('Kohli',66),('Ashwin',90)])) 
should return ['Kohli'] because Kohli's difference is 66 (73 - 7), Ashwin's difference is 57 (90 - 33) and 
Pujara's difference is 0 (122 - 122).
"""

def big(l):
	a = 0
	for i in l:
		if a < i:
			a = i
	return a

def small(l):
	a = 1000000
	for i in l:
		if i < a:
			a = i
	return a

def maxdifference(l):
	if len(l) == 0:
		return []
	if len(l) == 1:
		return [l[0][0]]
	names = []
	for i in l:
		if i[0] not in names:
			names.append(i[0])
	# print(names)
	# names.sort()
	d = {i : [] for i in names}
	# print(d)
	for i in l:
		d[i[0]].append(i[1])
	# print(d)
	maxdiff = 0
	res = []
	for i in d:
		curr = big(d[i]) - small(d[i])
		# print(big(d[i]), small(d[i]))
		if curr == maxdiff:
			res.append(i)
			# print(res)
		if maxdiff < curr:
			res = [i]
			maxdiff = curr
			# res.append(i)
	res.sort()
	return res

print(maxdifference([('Kohli',73),('Ashwin',33),('Kohli',7),('Pujara',122),('Kohli',66),('Ashwin',90)]))
print(maxdifference([('Kohli',73),('Ashwin',32),('Pujara',75),('Ashwin',44),('Kohli',7),('Pujara',22),('Ashwin',98),('Kolhi',68)]))
print(maxdifference([('Kohli', 89)]))
"""
Write a Python function aboveaverage(l) that takes a list of pairs of the form (name,score) as argument, 
where name is a string and score is an integer. Each pair is to be interpreted as the score of the named player.
For instance, an input of the form [('Kohli',73),('Ashwin',33),('Kohli',7),('Pujara',122),('Ashwin',90)] 
represents two scores of 73 and 7 for Kohli, two scores of 33 and 90 for Ashwin and one score of 122 for Pujara.
Your function should compute the list of players whose individual average score is greater than or equal to 
the overall average score. For an individual player, the average score is the total across all scores 
for that player divided by number of entries for that player. The overall average score is the total across 
all scores for all the players divided by the total number of entries across all players. 
The list should be sorted in ascending order by the name of the player.

For instance, aboveaverage([('Kohli',73),('Ashwin',33),('Kohli',7),('Pujara',122),('Ashwin',90)])
should return ['Pujara'] because the overall average score is 65 (325 divided by 5), 
Kohli's average is 40, (80 divided by 2), Ashwin's average is 61.5 (123 divided by 2) and 
Pujara's average is 122 (122 divided by 1).
"""
def aboveaverage(l):
	if len(l) == 0:
		return []
	if len(l) < 2:
		return [l[0][0]]
	match = {new_list[0] : [] for new_list in l}
	scores_of_matches = []
	for i in l:
		match[i[0]].append(i[1])
	count = 0
	for i in match:
		scores_of_matches.append([])
		for j in match[i]:
			scores_of_matches[count].append(j)
		count += 1
	total_avg = 0
	# For individual_avg average of each player
	individual_avg = []
	for i in range(len(scores_of_matches)):
		avg = 0
		for j in scores_of_matches[i]:
			avg += j / len(scores_of_matches[i])
		individual_avg.append(avg)
	# print(individual_avg)
	# For total average of all players
	d = {i : 0 for i in match.keys()}
	count = 0
	for i in d:
		d[i] = individual_avg[count]
		count += 1
	# print(d)
	for i in scores_of_matches:
		for j in i:
			total_avg += (j / len(l))
	# print(total_avg)
	# Calculating which value of dict.keys is greater than the total_avg
	res = []
	for i in d:
		if int(d[i]) >= int(total_avg):
			res.append(i)
	res.sort()
	return res
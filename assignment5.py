""""
Here are some basic facts about tennis scoring: A tennis match is made up of sets. A set is made up of games.

To win a set, a player has to win 6 games with a difference of 2 games. At 6-6, there is often a special tie-breaker.
In some cases, players go on playing till one of them wins the set with a difference of two games.

Tennis matches can be either 3 sets or 5 sets. The player who wins a majority of sets wins the match (i.e., 2 out 3 sets
or 3 out of 5 sets) The score of a match lists out the games in each set, with the overall winner's score reported first
for each set. Thus, if the score is 6-3, 5-7, 7-6 it means that the first player won the first set by 6 games to 3, lost
the second one 5 games to 7 and won the third one 7 games to 6 (and hence won the overall match as well by 2 sets to 1).

You will read input from the keyboard (standard input) containing the results of several tennis matches. Each match's
score is recorded on a separate line with the following format:

Winner:Loser:Set-1-score,...,Set-k-score, where 2 ≤ k ≤ 5

For example, an input line of the form

Osaka:Barty:3-6,6-3,6-3
indicates that Osaka beat Barty 3-6, 6-3, 6-3 in a best of 3 set match.

The input is terminated by a blank line.

You have to write a Python program that reads information about all the matches and compile the following
statistics for each player:

Number of best-of-5 set matches won
Number of best-of-3 set matches won
Number of sets won
Number of games won
Number of sets lost
Number of games lost
You should print out to the screen (standard output) a summary in decreasing order of ranking,
where the ranking is according to the criteria 1-6 in that order (compare item 1, if equal compare item 2,
if equal compare item 3 etc, noting that for items 5 and 6 the comparison is reversed).
"""""
import random as rn
# import


def winners(contents):
    # Splitting the list to extract winners list
    sl = []
    for i in contents:
        sl.append(i.split(":"))
    # print(sl)
    # Extracting winners list
    win = []
    for i in sl:
        if i[0] not in win:
            win.append(i[0])
    # Removing duplicates
    return win


def losers(contents):
    sl = []
    for i in contents:
        sl.append(i.split(":"))
    # print(sl)
    loss = []
    for i in sl:
        if i[1] not in loss:
            loss.append(i[1])
    return loss

def bestOf5(contents):
    sl = []
    for i in contents:
        sl.append(i.split(":"))
    print(sl)
    win_list = winners(contents)
    scores = dict.fromkeys(win_list, 0)
    print(scores)
    # for i in sl:

    # for i in sl:
    #     scores.append(i[2].split(","))
    # print(scores)

def bestOf3(contents):
    pass

def setsWon(contents):
    pass

def setsLost(contents):
    pass

def gamesWon(contents):
    pass

def gamesLost(contents):
    pass

def solve(contents):
    winner_list = winners(contents)
    loser_list = losers(contents)
    best_of_f = bestOf5(contents)
    best_of_t = bestOf3(contents)
    no_of_sets_won = setsWon(contents)
    no_of_sets_lost = setsLost(contents)
    no_of_games_won = gamesWon(contents)
    no_of_games_lost = gamesLost(contents)
    pass

def main():
    contents = []
    while True:
        try:
            line = input()
        except EOFError:
            break
        contents.append(line)
    print(contents)
    solve(contents)

# main()
stats = {}
line = input()
while line:
    (wsets, lsets, wgames, lgames) = (0, 0, 0, 0)
    (winner, loser, setscores) = line.strip().split(':', 2)

    sets = setscores.split(',')
    for set in sets:
        (winstr, losestr) = set.split('-')
        win = int(winstr)
        lose = int(losestr)
        wgames += win
        lgames += lose
        if win > lose:
            wsets += 1
        else:
            lsets += 1
        for player in [winner, loser]:
            try:
                stats[player]
            except KeyError:
                stats[player] = [0, 0, 0, 0, 0, 0]
            if wsets >= 3:
                stats[winner][0] += 1
            else:
                stats[winner][1] += 1
            stats[winner][2] += wsets
            stats[winner][3] += wgames
            stats[winner][4] -= lsets
            stats[winner][5] -= lgames
            stats[loser][2] += lsets
            stats[loser][3] += lgames
            stats[loser][4] -= wsets
            stats[loser][5] -= wgames
            line = input()
        statlist = [(stat[0], stat[1], stat[2], stat[3], stat[5], name) for name in stats.keys() for stat in [stats[name]]]
        statlist.sort(reverse=True)
        for entry in statlist:
            print(entry[6], entry[0], entry[1]. entry[2], entry[3], -entry[4], -entry[5])
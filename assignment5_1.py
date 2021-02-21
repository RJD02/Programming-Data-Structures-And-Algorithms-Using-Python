stats = {}
line = input()
while line:
    (wsets, lsets, wgames, lgames) = (0, 0, 0, 0)
    (winner, loser, setscores) = line.strip().split(':', 2)
    # print(winner, loser, setscores)
    sets = setscores.split(',')
    for set in sets:
        (winstr, losestr) = set.split('-')
        win = int(winstr)
        lose = int(losestr)
        wgames = wgames + win
        lgames = lgames + lose
        if win > lose:
            wsets = wsets + 1
        else:
            lsets = lsets + 1
    for player in [winner, loser]:
        try:
            stats[player]
        except KeyError:
            stats[player] = [0, 0, 0, 0, 0, 0]
    if wsets >= 3:
        stats[winner][0] = stats[winner][0] + 1
    else:
        stats[winner][1] = stats[winner][1] + 1
    stats[winner][2] = stats[winner][2] + wsets
    stats[winner][3] = stats[winner][3] + wgames
    stats[winner][4] = stats[winner][4] - lsets
    stats[winner][5] = stats[winner][5] - lgames
    stats[loser][2] = stats[loser][2] + lsets
    stats[loser][3] = stats[loser][3] + lgames
    stats[loser][4] = stats[loser][4] - wsets
    stats[loser][5] = stats[loser][5] - wgames
    line = input()
statlist = [(stat[0], stat[1], stat[2], stat[3], stat[4], stat[5], name) for name in stats.keys() for stat in
            [stats[name]]]
statlist.sort(reverse=True)
for entry in statlist:
    print(entry[6], entry[0], entry[1], entry[2], entry[3], -entry[4], -entry[5])
def best(i, l):
    global stored_best
    if stored_best[i] != 0:
        return stored_best[i]
    if i == 0:
        stored_best[i] = 1
        return 1
    max_count = 1
    for j in range(i):
        if l[i] % l[j] == 0:
            if stored_best[j] != 0:
                temp = stored_best[j]
            else:
                temp = best(j, l)
            max_count = max(max_count, temp + 1)
    stored_best[i] = max_count
    return max_count

def solve(l):
    global stored_best
    max_count = 0
    for i in range(1, len(l)):
        max_count = max(max_count, best(i, l))
    return max_count

#  l = [2, 11, 16, 12, 36, 60, 71, 29, 144, 288, 129, 432, 993]
n = int(input())
l = []
stored_best = []
for i in range(n):
    l.append(int(input()))
    stored_best.append(0)
print(solve(l))

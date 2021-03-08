def LCW(s1, s2):
    if len(s1) == 0 or len(s2) == 0:
        return 0
    if s1 == s2:
        return len(s1)
    maxcount = 0
    for i in range(len(s1)):
        for j in range(len(s2)):
            if s1[i] == s2[j]:
                count = 0
                start_s1 = i
                start_s2 = j
                while(start_s1 < len(s1) and start_s2 < len(s2) and s1[start_s1] == s2[start_s2]):
                    start_s1 += 1
                    start_s2 += 1
                    count += 1
                maxcount = max(count, maxcount)
    return maxcount

s1, s2 = input().split(" ")
print(LCW(s1, s2))

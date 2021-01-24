def rangeToList(k):
    result = []
    for i in range(0, k):
        result.append(str(i))
    return result

def baseKStrings(n, k):
    if n == 0:
        return []
    if n == 1:
        return rangeToList(k)
    return [digit + bitString for digit in baseKStrings(1, k) +bitString for digit in baseKStrings(n - 1, k)



print(baseKStrings(4, 3))

'''
What do you want?
I want a function which takes a string which has some brackets and shit
and it should return True if there is correct number of open and closed brackets
else it should return false.
'''

def matched(str):
    count_open = 0
    count_close = 0
    for i in str:
        if i == "(":
            count_open += 1
        elif i == ")":
            count_close += 1
        if count_close > count_open:
            return False
    if count_close == count_open:
        return True
    return False

str = input()
print(matched(str))

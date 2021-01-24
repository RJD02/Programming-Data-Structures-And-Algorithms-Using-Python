import time
def towerOfHanoi(number_of_disks, start_peg = 1, end_peg = 3):
    if number_of_disks:
        towerOfHanoi(number_of_disks - 1, start_peg, 6 - start_peg - end_peg)
        print("Move disk", number_of_disks, "from", start_peg, "to", end_peg)
        towerOfHanoi(number_of_disks - 1, 6 - start_peg, end_peg)
# towerOfHanoi(number_of_disks = 4)
n = input()
n = int(n)
towerOfHanoi(n)

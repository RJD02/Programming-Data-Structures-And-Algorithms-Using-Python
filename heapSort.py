def heapify(arr, n, i):
	largest = i # Initialize largest as root
	l = 2 * i + 1	 # left = 2*i + 1
	r = 2 * i + 2	 # right = 2*i + 2

	if l < n and arr[largest] < arr[l]:
		largest = l

	if r < n and arr[largest] < arr[r]:
		largest = r

	if largest != i:
		arr[i], arr[largest] = arr[largest], arr[i] # swap
		for i in range(len(arr)):
			print(arr[i], end = " ")
		print()
		heapify(arr, n, largest)


def heapSort(arr):
	n = len(arr)

	for i in range(n//2 - 1, -1, -1):
		heapify(arr, n, i)

	for i in range(n-1, 0, -1):
		arr[i], arr[0] = arr[0], arr[i] # swap
		heapify(arr, i, 0)
		# for j in range(len(arr)):
		# 	print(arr[j], end = " ")
		# print()


def main():
    arr = list(input().split(" "))
    for i in range(len(arr)):
        arr[i] = int(arr[i])
    heapSort(arr)
    for i in range(len(arr)):
        print("%d" % arr[i], end = " ")

main()

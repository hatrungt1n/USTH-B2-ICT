# Given a list of integers, determine the number of comparisons used by the bubble sort

def bubbleSort(arr):
	n = len(arr)
	for i in range(1, n):
		for j in range(1, n-i):
			if arr[j] > arr[j+1]:
				arr[j], arr[j+1] = arr[j+1], arr[j]

array = [10, 80, 30, 50, 80, 120, 130]
bubbleSort(array)

print ("Sorted array is: ",end="")
for i in range(len(array)):
	print (array[i],end=" ")

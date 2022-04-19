# Given a list of integers, determine the number of comparisons used by the insertion sort

def insertionSort(arr):
    n = len(arr)
    for i in range(n):
        j = i-1
        while j >= 0 and arr[i] < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = arr[i]

array = [10, 80, 30, 50, 80, 120, 130]
insertionSort(array)

print ("Sorted array is: ",end="")
for i in range(len(array)):
	print (array[i],end=" ")
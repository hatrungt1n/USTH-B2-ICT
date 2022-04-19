# Given an ordered list of n distinct integers, determine the position of an integer in the list
# using a binary search.

def binarySearch(array, x, low, high):

    while low <= high:

        mid = low + (high - low)//2

        if array[mid] == x:
            return mid

        elif array[mid] < x:
            low = mid + 1

        else:
            high = mid - 1

    return -1

array = [10, 20, 30, 40, 80, 120, 130]
x = 120

result = binarySearch(array, x, 0, len(array)-1)

if result == -1:
    print("Not found")
else:
    print("Element is present at index " + str(result))
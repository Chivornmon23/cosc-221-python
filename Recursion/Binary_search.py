def recursiveBinarySearch(lst, key):
    low = 0
    high = len(lst) - 1
    return recursiveBinarySearchHelper(lst, key, low, high)

def recursiveBinarySearchHelper(lst, key, low, high):
    if low > high: 
        return  -low - 1

    mid = (low+high)//2
    if key < lst[mid]: 
        return recursiveBinarySearchHelper(lst, key, low, mid -1)
    elif key == lst [mid]:
        return mid
    else: 
        return recursiveBinarySearchHelper(lst, key, mid + 1,high)

L = [3,2,5,1,2,6,3]
target = 6

print(f"Search for {target}: at index = {recursiveBinarySearch(L, target)}")

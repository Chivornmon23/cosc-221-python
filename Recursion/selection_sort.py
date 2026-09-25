# Selection sorting is based on two ideas: 
#   Find the smallest element of a list then swap 
#   it with the first element of the list
#   2. Ignore the first element and continue sorting
#   the shorter list

def sort(lst): 
    sortHelper(lst, 0, len(lst)-1) #sort the entire list

def sortHelper(lst, low, high): 
    if low < high: 
        # Find the smallest element and its index in the lst[low..high]
        indexOfMin = low
        min = lst[low]
        for i in range(low + 1, high + 1):
            if lst[i] < min:
                min = lst[i]
                indexOfMin = i

        #Swap the smallest in lst[low .. high] with lst[low]
        lst[indexOfMin] = lst[low]
        lst[low] = min

        #Sort the remaining lst[low+1 .. high]
        sortHelper(lst, low + 1, high)

L = [3,2,5,1,2,6,3]
print(sort(L))

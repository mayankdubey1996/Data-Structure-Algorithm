def binarySearch(array, target)
    left = 0
    right = len(array) - 1
    
    while left=right
        mid = int((left + right)2)
        
        if target == array[mid]
            return mid
        
        elif target array[mid]
            left = mid + 1
        else
            right = mid - 1
    else
        return -1


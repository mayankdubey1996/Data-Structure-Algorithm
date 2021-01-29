def binarySearch(array, target):
    left = 0
    right = len(array) - 1
    return binary_search_helper(array, target, left, right)

def binary_search_helper(array, target, left , right):
    mid = (left + right)//2
    
    
    if left>right:
        return -1
        
    elif target == array[mid]:
        return mid
        
    elif target> array[mid]:
        left = mid +1
        return  binary_search_helper(array, target, left , right)
    
    else:
        right = right - 1
        return  binary_search_helper(array, target, left, right)

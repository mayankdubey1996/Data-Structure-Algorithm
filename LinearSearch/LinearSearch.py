def linear_search(array, element):
    """array: list of numbers
       element: the number we want to search in the list"""
    
    for i in range(len(array)):
        if array[i] == element:
            return i
    return False

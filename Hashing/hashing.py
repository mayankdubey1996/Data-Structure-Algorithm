""" Time Complexity  
    To create hashTable O(n) 
    To get value from hashTable O(1)"""
    
    
""" Space complexity O(n) """


def hashing(array):
    h = {}
    for i in range(len(array)):
        value = array[i]
        idx = i
        h[value] = idx 
    return h
    
def search(hash_map, target):
    if target in hash_map:
        idx = hash_map[target]
        return idx
    return -1
    
array = [5,7,4,1,3,8]
hash_map = hashing(array)
z = search(hash_map, 1)
print(z)
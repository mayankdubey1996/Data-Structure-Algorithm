'''
-------------- Time Complexity  ---------------
# Best -> O(N)
# Average / Worst -> O(N^2)

-------------- Space Complexity --------------
O(1)
'''

def bubble_sort(array):
    for i in range(0,len(array)):
        for j in range(1, len(array)-i):
            if array[j-1] > array[j]:
                #swap
                array[j-1],array[j] = array[j], array[j-1]
    return array

array = [10,7,5,6,3,2]
z = bubble_sort(array)
print(z)

'''
################ Time ##################
Best/Average/Worst -> O(N^2)
################ Space ##################
O(1)'''

def selection_sort(array):
    for i in range(len(array)):
        minimum = array[i]
        min_idx = i
        for j in range(i, len(array)):
            if array[j]<minimum:
                minimum = array[j]
                min_idx = j
        array[i],array[min_idx] = array[min_idx],array[i]
    return array


array = [4,3,1,6,8,5]
z = selection_sort(array)
print(z)
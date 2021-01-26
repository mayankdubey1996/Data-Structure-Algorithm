#### space  - O(1) ####
#### Time ####

#Best: O(n)
#Average O(n^2)
#Worst O(n^2)

def insertion_sort(array):
    for i in range(1, len(array)):
        j= i-1
        while (j>-1) and (array[j]> array[j+1]):
            array[j],array[j+1] = array[j+1],array[j]
            j = j-1
    return array

array = [4,3,1,6,8,5]
z = insertion_sort(array)
print(z)
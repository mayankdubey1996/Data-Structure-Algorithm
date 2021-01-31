def partition(arr, r, l):
    pivot = l-1
    while l<=r:
        if arr[l]>arr[pivot] and arr[r]<arr[pivot]:
            arr[l],arr[r] = arr[r], arr[l]
            l = l+1
            r = r-1
        elif arr[l]<arr[pivot] and arr[r] < arr[pivot]:
            l = l+1
        elif arr[l]>arr[pivot] and arr[r]>arr[pivot]:
            r = r-1
        else:
            l=l+1
            r=r-1
    if l>r:
        arr[pivot],arr[r] = arr[r],arr[pivot]
    return r

def quick_sort(arr,r,l):
    if l<r:
      partitionIdx = partition(arr, r, l)
      quick_sort (arr,partitionIdx-1,l) #left
      quick_sort(arr,r, partitionIdx+2)  #right
      
def quick_sort_helper(arr):
    if len(arr)<1:
        return arr
    l = 1
    r = len(arr)-1
    quick_sort(arr,r,l)
    return arr

arr = [2, 7, 1, 4, 3]  
z=quick_sort_helper(arr)
print(z)


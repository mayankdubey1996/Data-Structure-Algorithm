def merge(arr,l,r,mid):
    temp = []
    i=l
    j=mid+1
    k=0
    
    while(i<=mid and j<=r):
        if arr[i]<=arr[j]:
            temp.append(arr[i])
            i = i+1
        else:
            temp.append(arr[j])
            j = j+1
    while(i<=mid):
        temp.append(arr[i])
        i=i+1
    while(j<=r):
        temp.append(arr[j])
        j=j+1
    for i in range(l,r+1):
        arr[i] = temp[i-l] 
    return arr
    
def merge_sort(arr,l,r):
    if l<r:
        mid = (l+r)//2
        merge_sort(arr,l,mid)
        merge_sort(arr,mid+1,r)
        
        return merge(arr,l,r,mid)

def merge_sort_helper(arr):
    if len(arr)<2:
        return arr
    l = 0
    r = len(arr)-1
    arr=merge_sort(arr,l,r)
    return arr

arr = [8,4,3,10,6,7,6]
z = merge_sort_helper(arr)
print(z)
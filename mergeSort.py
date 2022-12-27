def mergeSort(arr):
    if len(arr)<=1:
        return arr
    mid = len(arr)//2
    left = arr[:mid]
    right = arr[mid:]
    mergeSort(left)
    mergeSort(right)
    print(left,right,arr)
    merge_two_sorted(left, right, arr)

def merge_two_sorted(a,b, arr):
    len_a = len(a)
    len_b = len(b)
    i=j=k=0

    while i < len_a and j < len_b:
        if a[i]<=b[j]:
            arr[k]=a[i]
            i+=1
        else:
            arr[k]=b[j]
            j+=1
        k+=1
    while i<len_a:
        arr[k]=a[i]
        i+=1
        k+=1
    while j<len_b:
        arr[k]=b[j]
        j+=1
        k+=1


elements = [43,94,57,4,35,39,24,2,45,47,54,34,3,45,98]
mergeSort(elements)
print(elements)
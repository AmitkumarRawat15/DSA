def shellSort(arr):
    size = len(arr)
    gap = size//2
    print(gap)
    while gap>0:
        for i in range(gap,size):
            anchor = arr[i]
            j = i
            while j>=gap and arr[j-gap]>anchor:
                arr[j] = arr[j-gap]
                j-=gap
            arr[j] = anchor
        gap = gap//2
        print("**********")
        print(gap)
        print("*************")

elements = [21,38,29,17,4,25,11,32,9]
shellSort(elements)
print(elements)

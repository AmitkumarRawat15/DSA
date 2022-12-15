def partition(elements, start, end):
    pivot_index = start
    pivot = elements[start]
    while start<end:
        while start<len(elements) - 1 and elements[start]<=pivot:
            start += 1
        while elements[end]>pivot:
            end -= 1
        if start < end:
            elements[start], elements[end] = elements[end], elements[start]

    elements[pivot_index], elements[end] = elements[end],elements[pivot_index]

    return end

def quickSort(elements,start, end):
    if start < end:
        i = partition(elements,start,end)
        quickSort(elements,start,i)
        quickSort(elements,i+1,end)
        
elements = [11,7,29,2,15,28]
start = 0
end = len(elements)-1
result = quickSort(elements,start,end)
print(elements)
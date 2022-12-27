def selectionSort(mylist):
    size = len(mylist)
    for i in range(size):
        min_index = i
        for j in range(min_index+1,size):
            if mylist[j] < mylist[min_index]:
                min_index = j
        if i!=min_index:
            mylist[i],mylist[min_index]=mylist[min_index],mylist[i]

elements = [78,43,56,2,97,5,89,87,34]
selectionSort(elements)
print(elements)
def insertionSort(mylist):
    for i in range(1,len(mylist)):
        anchor = mylist[i]
        j = i - 1
        while j>=0 and anchor<mylist[j]:
            mylist[j+1]=mylist[j]
            j = j - 1
        mylist[j+1]=anchor
        
mylist=[100,38,1,46,37,95,47,76]
insertionSort(mylist)
print(mylist)
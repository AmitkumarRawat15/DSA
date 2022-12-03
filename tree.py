count = 2
input = 31
mylist = []
for i in range(count):
    mylist.append(input)
    input+=1



mydict = {}
for i in mylist:
    myresult = []
    test = []
    if mylist.index(i) == 0:
        num=1
        if mylist.index(i)+1 < len(mylist):
            while num <= mylist[mylist.index(i)]:
                newnum = int(str(i)+"0"+str(num))
                myresult.append(newnum)
                num+=1
        for x in myresult:
            if all([str(x).count(i) == 1 for i in set(str(x))]):
                test.append(x)
        mydict[i]=len(test)
    else:
        num=1
        if mylist.index(i) < len(mylist):
            res = 0 
            for j in mylist:
                if j > i:
                    break
                else:
                    res+=j
            while num <= res:
                newnum = int(str(i)+"0"+str(num))
                myresult.append(newnum)
                num+=1
        for x in myresult:
            if all([str(x).count(i) == 1 for i in set(str(x))]):
                test.append(x)
        mydict[i]=len(test)

print(mydict)
        

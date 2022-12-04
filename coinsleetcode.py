def arrangeCoins(n):
    i1 = 1
    while n>=i1:
        n = n-i1
        i1 += 1
    return i1-1



print(arrangeCoins(5))
def insertionSort(ar):
        
    for i in range(1,len(ar)):
        while i !=0 and ar[i] < ar[i-1]:
            ar[i], ar[i-1] = ar[i-1], ar[i]
            print ar
            i -= 1
    return ar

ar = [2,4,6,8,3]
print insertionSort(ar)
def insertionSort(arr):
    for i in range(len(arr)):
        print 'i',i
        x = arr[i]
        print 'x',x
        j = i-1
        print 'j',j
        while j >= 0 and arr[j] > arr[i]:
            arr[j+1] = arr[j] # this assigns new value
            arr[j] = x
            j -= 1
    return arr

arr = [1, -1, 5, 2, 88, 7]
print insertionSort(arr)
            
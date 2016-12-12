from collections import Counter 

def find_unique(lst):
    cnt = Counter()
    if len(lst) == 1:
        return lst[0]
    for num in lst:
        cnt[num] += 1
    return [key for key,value in cnt.iteritems() if value == 1][0]


print find_unique([1,1,2,3,3,6,6,7,7,11,11,15,15,19,19,20,20,20])

